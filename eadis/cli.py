"""Command-line entry point for the EADIS benchmark."""
import argparse
from pathlib import Path

import yaml

from agents.ollama_agent import OllamaAgent
from controller.config import AgentConfig
from eadis.extraction import mock, ollama, rules
from eadis.runner import run, write_report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, default=Path("datasets/eadis/inputs.jsonl"))
    parser.add_argument("--labels", type=Path, default=Path("datasets/eadis/labels.jsonl"))
    parser.add_argument("--mode", choices=["rule", "mock", "dry-run", "live"], default="rule")
    parser.add_argument("--worker", type=Path, action="append", default=[])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if len(args.worker) > 2 or (args.mode == "live" and not args.worker):
        parser.error("live mode requires one or two worker files")
    if args.worker and args.mode not in {"live", "dry-run"}:
        parser.error("worker files are supported in live and dry-run modes")
    try:
        configs = [AgentConfig.model_validate(yaml.safe_load(path.read_text(encoding="utf-8")))
                   for path in args.worker]
        if len({c.agent_id for c in configs}) != len(configs):
            raise ValueError("Worker IDs must be distinct")
        if len({c.endpoint for c in configs}) != len(configs):
            raise ValueError("Worker endpoints must be distinct")
        if configs:
            workers = {}
            for config in configs:
                agent = OllamaAgent(config)
                if args.mode == "live":
                    agent.verify_model()
                workers[config.agent_id] = (ollama(agent), config.model_dump())
        else:
            workers = {args.mode: (mock if args.mode == "mock" else rules, {})}
        report = run(args.inputs, args.labels, workers, args.mode)
        write_report(report, args.output)
    except (ValueError, KeyError, OSError, yaml.YAMLError) as error:
        parser.exit(2, f"eadis: {error}\n")
    if args.mode == "dry-run":
        return 0
    return int(any("error" in row or not row["incremental_agreement"]
                   for worker in report["workers"].values() for row in worker["steps"]))


if __name__ == "__main__":
    raise SystemExit(main())
