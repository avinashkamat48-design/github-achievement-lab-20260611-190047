from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal


ContributionKind = Literal["commit", "pull_request", "issue", "review", "docs"]


@dataclass(frozen=True)
class Contribution:
    """A planned or completed GitHub contribution."""

    title: str
    kind: ContributionKind
    summary: str
    impact: str
    evidence: list[str] = field(default_factory=list)
    tests: list[str] = field(default_factory=list)
    risks: list[str] = field(default_factory=list)

    def has_verification(self) -> bool:
        return bool(self.tests or self.evidence)

    def is_actionable(self) -> bool:
        return bool(self.title.strip() and self.summary.strip() and self.impact.strip())
