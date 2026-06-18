from __future__ import annotations

from achievement_lab.models import Contribution
from achievement_lab.scoring import score_contribution


def render_terminal_summary(contributions: list[Contribution]) -> list[str]:
    return [
        f"{score_contribution(contribution).total:3d} "
        f"{score_contribution(contribution).label:12s} "
        f"{contribution.title}"
        for contribution in contributions
    ]
