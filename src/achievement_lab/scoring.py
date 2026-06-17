from __future__ import annotations

from dataclasses import dataclass

from achievement_lab.models import Contribution


@dataclass(frozen=True)
class QualityScore:
    total: int
    label: str
    reasons: list[str]


def score_contribution(contribution: Contribution) -> QualityScore:
    score = 0
    reasons: list[str] = []

    if contribution.is_actionable():
        score += 30
        reasons.append("has a clear title, summary, and impact")
    if contribution.has_verification():
        score += 25
        reasons.append("includes verification evidence")
    if len(contribution.summary.split()) >= 8:
        score += 15
        reasons.append("summary has enough context")
    if contribution.risks:
        score += 15
        reasons.append("calls out risks or tradeoffs")
    if contribution.kind in {"pull_request", "review"} and contribution.tests:
        score += 15
        reasons.append("developer-facing work includes tests or checks")

    return QualityScore(total=score, label=_label(score), reasons=reasons)


def _label(score: int) -> str:
    if score >= 80:
        return "ready"
    if score >= 55:
        return "needs polish"
    return "not ready"
