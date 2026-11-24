"""Provision the EADIS issue hierarchy with an authenticated GitHub CLI."""
import argparse
import json
import re
import subprocess
import sys
import time
from collections import Counter
from graphlib import TopologicalSorter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "configs/research_issues.yaml"
INDEX = ROOT / "docs/issue_index.md"
README = ROOT / "README.md"
MARKER = re.compile(r"^<!-- eadis-task-id: ([A-Z0-9.]+) -->$", re.M)
HEADING = re.compile(r"^## ([A-Z0-9.]+) — (.+)$", re.M)
CHECK = re.compile(r"^- \[[ xX]\] (.+)$", re.M)
LINKS_START = "<!-- eadis-links:start -->"
LINKS_END = "<!-- eadis-links:end -->"
LINKS = re.compile(re.escape(LINKS_START) + r".*?" + re.escape(LINKS_END), re.S)
MASTER_LINK = "<!-- eadis-master-link -->"


class ApiError(RuntimeError):
    def __init__(self, message):
        super().__init__(message)
        match = re.search(r"HTTP (\d{3})", message)
        self.status = int(match[1]) if match else None


class GitHub:
    def __init__(self, repository):
        self.repo = f"repos/{repository}"

    @staticmethod
    def command(args, payload=None):
        process = subprocess.run(
            ["gh", *args], input=json.dumps(payload).encode("utf-8") if payload else None,
            capture_output=True, check=False,
        )
        if process.returncode:
            raise ApiError(process.stderr.decode("utf-8", errors="replace").strip())
        return process.stdout.decode("utf-8")

    def api(self, suffix="", method="GET", payload=None, pages=False):
        args = ["api", f"{self.repo}{suffix}", "--method", method]
        if pages:
            args += ["--paginate", "--slurp"]
        if payload is not None:
            args += ["--input", "-"]
        attempts = 3 if method == "GET" else 1
        for attempt in range(attempts):
            try:
                result = json.loads(self.command(args, payload))
                return [item for page in result for item in page] if pages else result
            except ApiError as error:
                retryable = error.status in {429, 500, 502, 503, 504} or (
                    error.status == 403 and "rate limit" in str(error).lower()
                )
                if not retryable or attempt + 1 == attempts:
                    raise
                time.sleep(30 * (attempt + 1))
        raise AssertionError("unreachable")

    def write(self, suffix, payload, method="POST"):
        # Keep write traffic below GitHub's secondary content-creation limit.
        time.sleep(1.0)
        return self.api(suffix, method, payload)


def unique(records, field):
    indexed = {record[field]: record for record in records}
    if len(indexed) != len(records):
        duplicates = [key for key, count in Counter(r[field] for r in records).items() if count > 1]
        raise ValueError(f"Duplicate {field}: {', '.join(map(str, duplicates))}")
    return indexed


def load_plan():
    plan = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    issues = unique(plan["issues"], "id")
    source = (ROOT / plan["checklist"]).read_text(encoding="utf-8")
    source = source.split("<!-- eadis-checklist-end -->", 1)[0]
    headings = list(HEADING.finditer(source))
    if len(headings) != len({heading[1] for heading in headings}):
        raise ValueError("Duplicate checklist headings")
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(source)
        section = source[heading.end():end]
        checks = CHECK.findall(section)
        if not checks or re.search(r"^- \[[xX]\]", section, re.M):
            raise ValueError(f"{heading[1]} must have unchecked checklist items")
        issues[heading[1]].update(name=heading[2], checks=checks)
    if set(issues) != {heading[1] for heading in headings}:
        raise ValueError("Manifest and checklist IDs differ")
    for task in issues.values():
        references = [*task["blocked_by"], *([task["parent"]] if task.get("parent") else [])]
        if set(references) - set(issues):
            raise ValueError(f"Unknown issue reference in {task['id']}")
        if set(task["labels"]) - set(plan["labels"]):
            raise ValueError(f"Unknown label in {task['id']}")
        if task.get("file") and not (ROOT / task["file"]).is_file():
            raise ValueError(f"Missing related file in {task['id']}: {task['file']}")
        if "milestone" in task and not 0 <= task["milestone"] < len(plan["milestones"]):
            raise ValueError(f"Invalid milestone in {task['id']}")
    for graph in ({key: task["blocked_by"] for key, task in issues.items()},
                  {key: [task["parent"]] if task.get("parent") else []
                   for key, task in issues.items()}):
        list(TopologicalSorter(graph).static_order())
    return plan, issues


def issue_body(task, plan):
    task_id = task["id"]
    source = f"https://github.com/{plan['repository']}/blob/{plan['documentation_ref']}/"
    phase = task.get("phase", "—")
    experiment = task.get("experiment") or "—"
    status = "Backlog" if task["scope"] == "optional" else "Not Started"
    checklist = "\n".join(f"- [ ] {check}" for check in task["checks"])
    related_file = task.get("file", "docs/eadis/research_log.md")
    if task.get("overview") or "type: task" not in task["labels"]:
        return f"""<!-- eadis-task-id: {task_id} -->
## Mục tiêu và động lực

{task.get("overview", task["name"])}

- Học và chuẩn bị · {task.get("learning", "Đọc giao thức và đối chiếu bằng chứng.")}
- Sản phẩm · {task.get("deliverable", "Bằng chứng, giới hạn và kết luận có thể kiểm chứng.")}
- RQ · {task.get("rq") or "Đọc theo phạm vi công việc."}
- Priority · {task["priority"]}
- Trạng thái ban đầu · {status}

## Completion gate

{checklist}

Đối chiếu kết quả với [bản đồ chuyển giao ETVM-PI]({source}docs/eadis/research_log.md#bản-đồ-chuyển-giao). Xem [tài liệu liên quan]({source}{related_file}) và [roadmap]({source}docs/eadis/learning_roadmap.md).
"""
    work = "Learning checklist" if task["kind"] in {"theory", "literature", "learning"} else "Checklist thực hiện và kiểm chứng"
    return f"""<!-- eadis-task-id: {task_id} -->
# Task Overview

- Task ID · {task_id}
- Phase · {phase}
- Experiment · {experiment}
- Category · {task["kind"]}
- Priority · {task["priority"]}
- Trạng thái ban đầu · {status}

## Mục tiêu và động lực

Hoàn thành **{task["name"]}** trong phạm vi {phase if phase != "—" else task["scope"]}. Công việc cung cấp một phần bằng chứng để xem xét kết quả của issue cha.

## Điều kiện chuẩn bị

Đọc [tài liệu liên quan]({source}{related_file}) và xem các prerequisite đã liên kết. Xác định giả định, đầu vào và điều kiện nào có thể bác bỏ kết quả.

## {work}

{checklist}

## Sản phẩm và tiêu chí chấp nhận

Mỗi mục cần có sản phẩm truy được và được người thực hiện đối chiếu với yêu cầu. Đính bài giải, note, code/test hoặc kết quả run theo tính chất công việc. Ghi assumptions và điều kiện chưa kiểm chứng.

## Research Reflection

Điều gì đã học được từ bằng chứng? Ca biên hoặc phản ví dụ nào làm thay đổi diễn giải? Câu hỏi nào còn mở và điều kiện nào cần cho [chuyển giao ETVM-PI]({source}docs/eadis/research_log.md#bản-đồ-chuyển-giao)?

## Completion Evidence

- Commit:
- Run ID:
- Dataset version:
- Research notes:
- Verification results:
- Completion date:
"""


def inventory(api, tasks):
    remote_labels = unique(api.api("/labels?per_page=100", pages=True), "name")
    milestones = unique(api.api("/milestones?state=all&per_page=100", pages=True), "title")
    remote = {}
    planned_titles = {task["title"] for task in tasks.values()}
    for item in api.api("/issues?state=all&per_page=100", pages=True):
        if "pull_request" in item:
            continue
        markers = MARKER.findall(item.get("body") or "")
        if len(markers) > 1:
            raise ValueError(f"Multiple EADIS markers on #{item['number']}")
        if markers:
            task_id = markers[0]
            if task_id in remote or task_id not in tasks:
                raise ValueError(f"Duplicate or unexpected EADIS ID {task_id}")
            remote[task_id] = item
        elif item["title"] in planned_titles:
            raise ValueError(f"Unmanaged issue #{item['number']} has a planned title. Review it before provisioning.")
    return remote_labels, milestones, remote


def create_resources(api, plan, tasks, labels, milestones, remote):
    for name, color in plan["labels"].items():
        if name not in labels:
            labels[name] = api.write("/labels", {"name": name, "color": color})
    for milestone in plan["milestones"]:
        title = milestone["title"]
        if title not in milestones:
            milestones[title] = api.write("/milestones", milestone)
    for key, task in tasks.items():
        if key in remote:
            continue
        payload = {"title": task["title"], "body": issue_body(task, plan), "labels": task["labels"]}
        linked = related_keys(task, tasks)
        if linked and linked <= remote.keys():
            payload["body"] += "\n" + refs(task, tasks, remote) + "\n"
        if "milestone" in task:
            title = plan["milestones"][task["milestone"]]["title"]
            payload["milestone"] = milestones[title]["number"]
        remote[key] = api.write("/issues", payload)
        print(f"{key}: {remote[key]['html_url']}", flush=True)


def related_keys(task, tasks):
    return {
        *task["blocked_by"],
        *([task["parent"]] if task.get("parent") else []),
        *(key for key, candidate in tasks.items() if candidate.get("parent") == task["id"]),
    }


def refs(task, tasks, remote):
    def ref(key):
        return f"#{remote[key]['number']}"

    key = task["id"]
    children = [k for k, candidate in tasks.items() if candidate.get("parent") == key]
    lines = [LINKS_START]
    if task.get("parent"):
        lines += ["", f"Parent: {ref(task['parent'])}"]
    if children:
        lines += ["", "## Roadmap và công việc liên quan", ""]
        lines += [f"- [ ] {ref(k)} · {tasks[k]['name']}" for k in children]
    if task["blocked_by"]:
        lines += ["", "## Blocked by", ""]
        lines += [f"- {ref(k)} · {tasks[k]['name']}" for k in task["blocked_by"]]
    if lines == [LINKS_START]:
        return ""
    return "\n".join([*lines, "", LINKS_END])


def normalized_links(body):
    return re.sub(r"(?m)^- \[[xX]\]", "- [ ]", body).strip()


def sync_links(api, tasks, remote, apply):
    failures = []
    for key, task in tasks.items():
        expected = refs(task, tasks, remote)
        if not expected:
            continue
        number = remote[key]["number"]
        path = f"/issues/{number}"
        body = remote[key].get("body") or ""
        matches = LINKS.findall(body)
        if matches and len(matches) == 1 and normalized_links(matches[0]) == expected:
            continue
        if not matches and LINKS_START not in body and LINKS_END not in body and apply:
            current = api.api(path).get("body") or ""
            if current == body and remote[key]["state"] == "open":
                api.write(path, {"body": body.rstrip() + "\n\n" + expected + "\n"}, method="PATCH")
                continue
        failures.append(f"{key}: missing or edited managed links on #{number}")
    return failures


def native_relationships(api, tasks, remote, apply):
    missing = []
    modes = {}
    for endpoint, payload_key, relation in [
        ("sub_issues", "sub_issue_id", "children"),
        ("dependencies/blocked_by", "issue_id", "blocked_by"),
    ]:
        desired = (
            {k: [child for child, task in tasks.items() if task.get("parent") == k] for k in tasks}
            if relation == "children" else {k: task["blocked_by"] for k, task in tasks.items()}
        )
        modes[relation] = "native"
        for key, targets in desired.items():
            if not targets:
                continue
            path = f"/issues/{remote[key]['number']}/{endpoint}"
            try:
                existing = {item["id"] for item in api.api(path + "?per_page=100", pages=True)}
            except ApiError as error:
                if error.status in {404, 405, 410, 501}:
                    modes[relation] = "Markdown fallback"
                    break
                raise
            for target in targets:
                if remote[target]["id"] in existing:
                    continue
                if apply:
                    api.write(path, {payload_key: remote[target]["id"]})
                else:
                    missing.append(f"{key}: missing native {relation} link to {target}")
    print("Relationships:", json.dumps(modes))
    return missing


def verify_records(plan, tasks, labels, milestones, remote):
    problems = []
    for name in plan["labels"].keys() - labels.keys():
        problems.append(f"Missing label: {name}")
    for milestone in plan["milestones"]:
        if milestone["title"] not in milestones:
            problems.append(f"Missing milestone: {milestone['title']}")
    for key, task in tasks.items():
        if key not in remote:
            problems.append(f"Missing issue: {key}")
            continue
        item = remote[key]
        if CHECK.findall((item.get("body") or "").split(LINKS_START, 1)[0]) != task["checks"]:
            problems.append(f"{key}: checklist text differs")
        expected = {name for name in task["labels"] if not name.startswith("status: ")}
        actual = {label["name"] for label in item["labels"]}
        if not expected <= actual or not any(name.startswith("status: ") for name in actual):
            problems.append(f"{key}: labels differ")
        if "milestone" in task:
            title = plan["milestones"][task["milestone"]]["title"]
            if (item.get("milestone") or {}).get("title") != title:
                problems.append(f"{key}: milestone differs")
    return problems


def write_index(plan, tasks, remote):
    lines = [
        "# EADIS GitHub Issue Index", "",
        "Trạng thái và completion evidence được theo dõi trong từng GitHub Issue.", "",
        "| Task ID | Task Name | GitHub Issue | Parent Issue | Milestone | Priority |",
        "|---|---|---|---|---|---|",
    ]

    def link(key):
        record = remote[key]
        return f"[#{record['number']}]({record['html_url']})"

    for key, task in tasks.items():
        parent = link(task["parent"]) if task.get("parent") else "—"
        milestone = plan["milestones"][task["milestone"]]["title"] if "milestone" in task else "—"
        lines.append(f"| {key} | {task['name']} | {link(key)} | {parent} | {milestone} | {task['priority']} |")
    INDEX.write_text("\n".join(lines) + "\n", encoding="utf-8")
    readme = README.read_text(encoding="utf-8")
    master = f"- [Master Tracking Issue]({remote['MASTER']['html_url']})"
    if MASTER_LINK in readme:
        README.write_text(readme.replace(MASTER_LINK, master, 1), encoding="utf-8")
    elif master not in readme:
        raise ValueError("Master link in README differs. Review existing link before updating.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    for mode in ("dry-run", "apply", "verify"):
        modes.add_argument("--" + mode, action="store_true")
    args = parser.parse_args()
    try:
        plan, tasks = load_plan()
        print(f"Plan: {len(tasks)} issues, {len(plan['labels'])} labels, "
              f"{len(plan['milestones'])} milestones, "
              f"{sum(len(task['checks']) for task in tasks.values())} checklist items.", flush=True)
        if args.dry_run:
            return 0
        GitHub.command(["auth", "status", "--hostname", "github.com"])
        api = GitHub(plan["repository"])
        repository = api.api()
        if not repository["has_issues"]:
            raise ValueError("GitHub Issues are disabled for the repository")
        if args.apply and not repository.get("permissions", {}).get("push"):
            raise ValueError("Authenticated account needs write access for issue labels and milestones")
        labels, milestones, remote = inventory(api, tasks)
        print(f"Existing managed issues: {len(remote)}. "
              f"Labels to create: {len(plan['labels'].keys() - labels.keys())}. "
              f"Milestones to create: {sum(m['title'] not in milestones for m in plan['milestones'])}.",
              flush=True)
        if args.apply:
            create_resources(api, plan, tasks, labels, milestones, remote)
        failures = verify_records(plan, tasks, labels, milestones, remote)
        if not failures:
            failures.extend(sync_links(api, tasks, remote, args.apply))
            failures.extend(native_relationships(api, tasks, remote, args.apply))
        if args.apply and not failures:
            labels, milestones, remote = inventory(api, tasks)
            failures.extend(verify_records(plan, tasks, labels, milestones, remote))
            failures.extend(sync_links(api, tasks, remote, False))
            failures.extend(native_relationships(api, tasks, remote, False))
        if failures:
            raise ValueError("\n".join(failures))
        write_index(plan, tasks, remote)
        print(f"Verified {len(remote)} managed issues. MASTER: {remote['MASTER']['html_url']}")
        return 0
    except (ValueError, RuntimeError, OSError, KeyError, yaml.YAMLError) as error:
        print(f"EADIS setup: {error}", file=sys.stderr)
        if args.apply:
            print("Check permissions, connectivity and GitHub rate limits before rerunning --apply. "
                  "The next run will rediscover successful writes.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
