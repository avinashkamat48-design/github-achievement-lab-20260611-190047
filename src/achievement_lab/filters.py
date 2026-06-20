from __future__ import annotations

from achievement_lab.models import Contribution
from achievement_lab.scoring import score_contribution


def filter_by_min_score(contributions: list[Contribution], min_score: int | None) -> list[Contribution]:
    if min_score is None:
        return contributions
    return [contribution for contribution in contributions if score_contribution(contribution).total >= min_score]
