from __future__ import annotations

import csv
from pathlib import Path

from achievement_lab.models import Contribution
from achievement_lab.scoring import score_contribution


CSV_FIELDS = ["title", "kind", "score", "label", "impact"]


def write_csv(path: Path, contributions: list[Contribution]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for contribution in contributions:
            score = score_contribution(contribution)
            writer.writerow(
                {
                    "title": contribution.title,
                    "kind": contribution.kind,
                    "score": score.total,
                    "label": score.label,
                    "impact": contribution.impact,
                }
            )
