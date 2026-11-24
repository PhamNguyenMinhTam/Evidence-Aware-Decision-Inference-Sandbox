"""Exact provenance checks and finite constraint inference."""
from dataclasses import dataclass

from eadis.schema import Case, Claim, Source


@dataclass(frozen=True)
class Evidence:
    kind: str
    subject: str
    object: str | None
    source_id: str
    start: int
    end: int


def validate(case: Case, sources: list[Source], claim: Claim) -> Evidence | None:
    texts = {source.id: source.text for source in sources}
    text = texts.get(claim.source_id, "")
    start = text.find(claim.quote)
    if start < 0 or not claim.quote.strip():
        return None
    if claim.kind == "before":
        if claim.subject not in case.events or claim.object not in case.events:
            return None
    elif claim.subject not in case.options or claim.object is not None:
        return None
    return Evidence(claim.kind, claim.subject, claim.object, claim.source_id,
                    start, start + len(claim.quote))


class EvidenceStore:
    def __init__(self, options: list[str]):
        self.universe = set(options)
        self.possible = set(options)
        self.records: set[Evidence] = set()
        self.before: set[tuple[str, str]] = set()

    def add(self, evidence: Evidence) -> None:
        if evidence in self.records:
            return
        self.records.add(evidence)
        if evidence.kind == "selected":
            self.possible.intersection_update({evidence.subject})
        elif evidence.kind == "excluded":
            self.possible.discard(evidence.subject)
        else:
            start, end = evidence.subject, evidence.object
            predecessors = {start} | {a for a, b in self.before if b == start}
            successors = {end} | {b for a, b in self.before if a == end}
            self.before.update((a, b) for a in predecessors for b in successors)

    def result(self) -> dict:
        temporal_conflict = any(a == b for a, b in self.before)
        return {
            "possible": sorted(self.possible),
            "possible_if_conflicted": sorted(self.universe if not self.possible else self.possible),
            "before": sorted(self.before),
            "decision_conflict": not self.possible,
            "temporal_conflict": temporal_conflict,
            "status": (
                "conflict" if temporal_conflict or not self.possible
                else "identified" if len(self.possible) == 1
                else "underdetermined"
            ),
        }


def recompute(options: list[str], records: list[Evidence]) -> dict:
    """Independent oracle using whole-prefix filtering and fixed-point closure."""
    store = EvidenceStore(options)
    selected = {item.subject for item in records if item.kind == "selected"}
    excluded = {item.subject for item in records if item.kind == "excluded"}
    store.possible = {option for option in options if option not in excluded
                      and selected <= {option}}
    store.before = {(item.subject, item.object) for item in records if item.kind == "before"}
    while True:
        implied = {(a, d) for a, b in store.before for c, d in store.before if b == c}
        if implied <= store.before:
            return store.result()
        store.before.update(implied)
