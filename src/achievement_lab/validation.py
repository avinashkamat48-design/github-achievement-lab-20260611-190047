from __future__ import annotations

from dataclasses import dataclass

from achievement_lab.models import Contribution


@dataclass(frozen=True)
class PlanIssue:
    title: str
    severity: str
    message: str


def validate_contributions(contributions: list[Contribution]) -> list[PlanIssue]:
    issues: list[PlanIssue] = []
    for contribution in contributions:
        if len(contribution.summary.split()) < 8:
            issues.append(
                PlanIssue(
                    title=contribution.title,
                    severity="warning",
                    message="summary is too short to explain the contribution clearly",
                )
            )
        if not contribution.has_verification():
            issues.append(
                PlanIssue(
                    title=contribution.title,
                    severity="error",
                    message="missing evidence or tests for verification",
                )
            )
        if contribution.kind in {"pull_request", "review"} and not contribution.risks:
            issues.append(
                PlanIssue(
                    title=contribution.title,
                    severity="warning",
                    message="developer-facing work should name risks or tradeoffs",
                )
            )
    return issues
