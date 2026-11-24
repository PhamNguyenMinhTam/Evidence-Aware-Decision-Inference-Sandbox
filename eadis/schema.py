"""Public inputs, extractor outputs and evaluation-only labels."""
from typing import Literal, Self

from pydantic import Field, model_validator

from controller.config import StrictModel

Identifier = str


class Source(StrictModel):
    id: Identifier = Field(min_length=1)
    text: str = Field(min_length=1)


class DecisionContext(StrictModel):
    actor: str = Field(min_length=1)
    situation: str = Field(min_length=1)
    options: list[str] = Field(min_length=2)
    events: list[str]


class Case(DecisionContext):
    id: Identifier = Field(min_length=1)
    family: str = Field(min_length=1)
    condition: str = Field(min_length=1)
    batches: list[list[Source]] = Field(min_length=1)

    @model_validator(mode="after")
    def unique_ids(self) -> Self:
        for values in (self.options, self.events, [s.id for b in self.batches for s in b]):
            if len(values) != len(set(values)) or any(not value.strip() for value in values):
                raise ValueError("IDs and options must be unique and nonblank within each namespace")
        return self


class Claim(StrictModel):
    source_id: Identifier
    quote: str = Field(min_length=1)
    kind: Literal["selected", "excluded", "before"]
    subject: Identifier
    object: Identifier | None = None


class Extraction(StrictModel):
    actor: str | None = None
    situation: str | None = None
    options: list[str] = Field(default_factory=list)
    action: str | None = None
    claims: list[Claim]


class GoldStep(StrictModel):
    extraction: Extraction
    possible: list[str]
    possible_if_conflicted: list[str]
    before: list[tuple[str, str]]
    conflict: bool


class GoldCase(StrictModel):
    id: Identifier
    steps: list[GoldStep]
