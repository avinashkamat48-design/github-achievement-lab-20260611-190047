from __future__ import annotations

from achievement_lab.models import Contribution


def recommend_next_steps(contribution: Contribution) -> list[str]:
    steps: list[str] = []
    if not contribution.summary.strip():
        steps.append("write a one-sentence summary of the change")
    if not contribution.impact.strip():
        steps.append("explain who benefits from the contribution")
    if not contribution.has_verification():
        steps.append("add a test command, reproduction step, or evidence link")
    if contribution.kind in {"pull_request", "review"} and not contribution.risks:
        steps.append("name a risk, tradeoff, or reason the change is safe")
    return steps
