from __future__ import annotations

from collections import Counter

from achievement_lab.models import Contribution
from achievement_lab.scoring import score_contribution


def render_terminal_summary(contributions: list[Contribution]) -> list[str]:
    return [
        f"{score_contribution(contribution).total:3d} "
        f"{score_contribution(contribution).label:12s} "
        f"{contribution.title}"
        for contribution in contributions
    ]


def summarize_by_kind(contributions: list[Contribution]) -> dict[str, int]:
    return dict(Counter(contribution.kind for contribution in contributions))


def summarize_by_label(contributions: list[Contribution]) -> dict[str, int]:
    return dict(Counter(score_contribution(contribution).label for contribution in contributions))
