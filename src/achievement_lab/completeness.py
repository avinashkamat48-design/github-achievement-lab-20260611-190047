from __future__ import annotations

from dataclasses import dataclass

from achievement_lab.models import Contribution


@dataclass(frozen=True)
class CompletenessSummary:
    total: int
    verified: int
    with_risks: int
    kinds: tuple[str, ...]

    @property
    def is_complete(self) -> bool:
        return self.total > 0 and self.verified == self.total and self.with_risks == self.total


def assess_completeness(contributions: list[Contribution]) -> CompletenessSummary:
    return CompletenessSummary(
        total=len(contributions),
        verified=sum(1 for contribution in contributions if contribution.has_verification()),
        with_risks=sum(1 for contribution in contributions if contribution.risks),
        kinds=tuple(sorted({contribution.kind for contribution in contributions})),
    )
