import json
from pathlib import Path

from agents.ollama_agent import OllamaAgent
from eadis import cli
from eadis.extraction import ollama, rules
from eadis.runner import run

FIXTURES = Path("datasets/eadis")


def test_pilot_inference_distinguishes_ambiguity_and_conflict():
    report = run(FIXTURES / "inputs.jsonl", FIXTURES / "labels.jsonl",
                 {"rule": (rules, {})}, "rule")
    rows = {(row["case"], row["step"]): row for row in report["workers"]["rule"]["steps"]}
    assert len(rows) == 11
    assert all(row["incremental_agreement"] for row in rows.values())
    assert all(row["metrics"]["temporal"]["f1"] == 1 for row in rows.values())
    assert rows["transport-missing", 0]["inference"]["possible"] == ["bus", "train"]
    assert rows["transport-conflict", 1]["inference"]["possible"] == []
    assert rows["transport-conflict", 1]["inference"]["decision_conflict"]
    assert rows["transport-cycle", 0]["inference"]["temporal_conflict"]
    assert rows["transport-incremental", 1]["metrics"]["temporal"]["f1"] == 1
    assert not rows["transport-paraphrase", 0]["metrics"]["set_exact"]


def test_live_prompt_sees_only_current_batch_and_provenance_is_validated():
    prompts = []

    def transport(url, payload, timeout):
        prompts.append(payload["messages"][1]["content"])
        assert payload["format"]["title"] == "Extraction"
        return {
            "done": True,
            "message": {"content": json.dumps({"claims": [
                {"source_id": "initial", "quote": "fabricated", "kind": "selected",
                 "subject": "train"},
            ]})},
        }

    class Config:
        endpoint = "http://test"
        model_name = "test"
        system_prompt = "JSON"
        inference = {}
        timeout = 1

    report = run(FIXTURES / "inputs.jsonl", FIXTURES / "labels.jsonl",
                 {"test": (ollama(OllamaAgent(Config(), transport)), {})}, "live")
    assert "Maya selected train." not in prompts[5]
    assert "Maya ruled out car." not in prompts[6]
    assert "Maya selected train." in prompts[6]
    assert all("possible_if_conflicted" not in prompt for prompt in prompts)
    row = report["workers"]["test"]["steps"][0]
    assert row["rejected_claims"] == 1
    assert row["evidence"] == []
    assert row["inference"]["status"] == "underdetermined"


def test_cli_runs_two_independent_workers(monkeypatch, tmp_path):
    from sys import argv

    from controller.config import AgentConfig
    from eadis.schema import DecisionContext, Source

    verified = []
    calls = []

    def make_agent(config):
        def transport(url, payload=None, timeout=120):
            if payload is None:
                verified.append(config.agent_id)
                return {"models": [{"name": "model", "digest": "digest",
                                    "details": {"quantization_level": "Q4"}}]}
            calls.append(config.agent_id)
            supplied = json.loads(payload["messages"][1]["content"].split("\nInput:\n", 1)[1])
            sources = [Source.model_validate(item) for item in supplied.pop("sources")]
            result = rules(DecisionContext.model_validate(supplied), sources)
            return {"done": True, "message": {"content": result.model_dump_json()}}

        return OllamaAgent(config, transport)

    monkeypatch.setattr(cli, "OllamaAgent", make_agent)
    worker_args = []
    for worker in ("a", "b"):
        config = AgentConfig(agent_id=worker, hardware_id=worker, endpoint=f"http://{worker}",
                             model_name="model", model_digest="digest", quantization="Q4",
                             prompt_version="test", system_prompt="JSON")
        path = tmp_path / f"{worker}.yaml"
        path.write_text(config.model_dump_json(), encoding="utf-8")
        worker_args.extend(["--worker", str(path)])
    output = tmp_path / "report.json"
    monkeypatch.setattr("sys.argv", [argv[0], "--mode", "live", *worker_args,
                                    "--output", str(output)])
    assert cli.main() == 0
    assert verified == ["a", "b"]
    assert calls == ["a"] * 11 + ["b"] * 11
    report = json.loads(output.read_text(encoding="utf-8"))
    assert set(report["workers"]) == {"a", "b"}
