"""Generate predictions on public fixtures before loading evaluation labels."""
import hashlib
import json
import platform
from pathlib import Path
from time import perf_counter_ns

from pydantic import ValidationError

from eadis.evaluation import score, summarize
from eadis.extraction import PROMPT_VERSION
from eadis.inference import EvidenceStore, recompute, validate
from eadis.schema import Case, DecisionContext, Extraction, GoldCase


def load_jsonl(content: bytes, schema) -> dict:
    entries = [schema.model_validate_json(line) for line in content.splitlines() if line.strip()]
    indexed = {entry.id: entry for entry in entries}
    if not entries or len(indexed) != len(entries):
        raise ValueError("JSONL must contain records with unique IDs")
    return indexed


def predict(case, extract):
    context = DecisionContext(actor=case.actor, situation=case.situation,
                              options=case.options, events=case.events)
    store = EvidenceStore(case.options)
    records = []
    rows = []
    failed_prefix = False
    for step, sources in enumerate(case.batches):
        row = {"case": case.id, "family": case.family, "condition": case.condition, "step": step}
        rows.append(row)
        if failed_prefix:
            row["error"] = "IncompleteEvidencePrefix"
            continue
        try:
            start = perf_counter_ns()
            extracted = extract(context, sources) if sources else Extraction(
                actor=context.actor, situation=context.situation, options=context.options, claims=[]
            )
            row["extraction_ns"] = perf_counter_ns() - start
        except (ValidationError, OSError, ValueError, KeyError) as error:
            failed_prefix = True
            row["error"] = type(error).__name__
            continue
        verified = [validate(case, sources, claim) for claim in extracted.claims]
        added = [record for record in verified if record is not None]
        records.extend(added)
        start = perf_counter_ns()
        for record in added:
            store.add(record)
        result = store.result()
        incremental_ns = perf_counter_ns() - start
        start = perf_counter_ns()
        full = recompute(case.options, records)
        full_ns = perf_counter_ns() - start
        row.update(
            extraction=extracted.model_dump(),
            evidence=[record.__dict__ for record in dict.fromkeys(records)],
            rejected_claims=len(verified) - len(added),
            inference=result,
            incremental_agreement=result == full,
            incremental_ns=incremental_ns,
            full_ns=full_ns,
        )
    return rows


def run(inputs: Path, labels: Path, workers: dict, mode: str) -> dict:
    public_bytes = inputs.read_bytes()
    cases = load_jsonl(public_bytes, Case)
    report = {
        "mode": mode,
        "prompt_version": PROMPT_VERSION,
        "python": platform.python_version(),
        "platform": platform.platform(),
        "inputs_sha256": hashlib.sha256(public_bytes).hexdigest(),
        "cases": list(cases),
        "workers": {},
    }
    if mode == "dry-run":
        report["planned_steps_per_worker"] = sum(len(case.batches) for case in cases.values())
        report["workers"] = {name: metadata for name, (_, metadata) in workers.items()}
        return report
    for name, (extract, metadata) in workers.items():
        rows = [row for case in cases.values() for row in predict(case, extract)]
        report["workers"][name] = {"config": metadata, "steps": rows}

    label_bytes = labels.read_bytes()
    gold = load_jsonl(label_bytes, GoldCase)
    if gold.keys() != cases.keys() or any(len(gold[k].steps) != len(c.batches) for k, c in cases.items()):
        raise ValueError("Evaluation labels must match public cases and step counts")
    report["labels_sha256"] = hashlib.sha256(label_bytes).hexdigest()
    for worker in report["workers"].values():
        for row in worker["steps"]:
            if "error" not in row:
                row["metrics"] = score(
                    Extraction.model_validate(row["extraction"]), row["inference"],
                    row["rejected_claims"], gold[row["case"]].steps[row["step"]],
                )
        worker["summary_by_condition"] = summarize(worker["steps"])
    return report


def write_report(report: dict, output: Path | None) -> None:
    content = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if output is None:
        print(content, end="")
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("x", encoding="utf-8", newline="\n") as destination:
            destination.write(content)
