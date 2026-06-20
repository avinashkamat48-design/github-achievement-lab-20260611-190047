from __future__ import annotations

from html import escape

from achievement_lab.models import Contribution
from achievement_lab.recommendations import recommend_next_steps
from achievement_lab.scoring import score_contribution


def render_html(contributions: list[Contribution]) -> str:
    rows = []
    for contribution in contributions:
        score = score_contribution(contribution)
        next_steps = "; ".join(recommend_next_steps(contribution)) or "none"
        rows.append(
            "<tr>"
            f"<td>{escape(contribution.title)}</td>"
            f"<td>{escape(contribution.kind)}</td>"
            f"<td>{score.total}</td>"
            f"<td>{escape(score.label)}</td>"
            f"<td>{escape(contribution.impact)}</td>"
            f"<td>{escape(next_steps)}</td>"
            "</tr>"
        )
    return "\n".join(
        [
            "<!doctype html>",
            "<html lang=\"en\">",
            "<head><meta charset=\"utf-8\"><title>Contribution Quality Report</title></head>",
            "<body>",
            "<h1>Contribution Quality Report</h1>",
            "<table>",
            "<thead><tr><th>Title</th><th>Kind</th><th>Score</th><th>Label</th><th>Impact</th><th>Next steps</th></tr></thead>",
            f"<tbody>{''.join(rows)}</tbody>",
            "</table>",
            "</body>",
            "</html>",
        ]
    )
