"""Metrics with explicit denominators and evaluation-only labels."""
from statistics import mean

from eadis.schema import Extraction, GoldStep


def prf(actual: set, expected: set) -> dict:
    matches = len(actual & expected)
    precision = matches / len(actual) if actual else float(not expected)
    recall = matches / len(expected) if expected else float(not actual)
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"precision": precision, "recall": recall, "f1": f1}


def score(extracted: Extraction, result: dict, rejected: int, gold: GoldStep) -> dict:
    def claim_keys(extraction):
        return {(c.kind, c.subject, c.object, c.source_id, c.quote) for c in extraction.claims}

    actual = claim_keys(extracted)
    expected = claim_keys(gold.extraction)
    decision = result["possible"]
    conflict = result["decision_conflict"] or result["temporal_conflict"]
    point = {extracted.action} if extracted.action is not None else set()
    return {
        "evidence": prf(actual, expected),
        "structural_valid_rate": (len(extracted.claims) - rejected) / len(extracted.claims)
        if extracted.claims else None,
        "actor_exact": extracted.actor == gold.extraction.actor,
        "situation_exact": extracted.situation == gold.extraction.situation,
        "options": prf(set(extracted.options), set(gold.extraction.options)),
        "point_baseline_exact": extracted.action == gold.extraction.action,
        "point_baseline_set_exact": point == set(gold.possible),
        "unconstrained_baseline_set_exact": set(gold.extraction.options) == set(gold.possible),
        "temporal": prf(set(result["before"]), set(gold.before)),
        "set_exact": set(decision) == set(gold.possible),
        "set_covers_gold": set(gold.possible) <= set(decision) if gold.possible else None,
        "conflict_exact": conflict == gold.conflict,
        "fallback_set_exact": set(result["possible_if_conflicted"]) == set(gold.possible_if_conflicted),
        "set_size": len(decision),
    }


def summarize(rows: list[dict]) -> dict:
    """Describe step-level results, grouped by condition."""
    groups = {}
    for row in rows:
        groups.setdefault(row["condition"], []).append(row)
    summary = {}
    for condition, group in sorted(groups.items()):
        successful = [r for r in group if "metrics" in r]
        summary[condition] = {
            "steps": len(group),
            "extraction_failures": len(group) - len(successful),
            "evidence_macro_f1": mean(r["metrics"]["evidence"]["f1"] for r in successful)
            if successful else None,
            "temporal_macro_f1": mean(r["metrics"]["temporal"]["f1"] for r in successful)
            if successful else None,
            "set_exact_rate": mean(r["metrics"]["set_exact"] for r in successful)
            if successful else None,
            "incremental_agreement_rate": mean(r["incremental_agreement"] for r in successful)
            if successful else None,
        }
    return summary
