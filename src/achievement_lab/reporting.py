from __future__ import annotations

from achievement_lab.models import Contribution
from achievement_lab.scoring import score_contribution


def render_markdown(contributions: list[Contribution]) -> str:
    lines = [
        "# Contribution Quality Report",
        "",
        "| Title | Kind | Score | Label |",
        "|---|---|---:|---|",
    ]

    for contribution in contributions:
        score = score_contribution(contribution)
        lines.append(
            f"| {_cell(contribution.title)} | {contribution.kind} | {score.total} | {score.label} |"
        )

    lines.extend(["", "## Details", ""])
    for contribution in contributions:
        score = score_contribution(contribution)
        lines.extend(
            [
                f"### {contribution.title}",
                "",
                f"- Kind: `{contribution.kind}`",
                f"- Impact: {contribution.impact}",
                f"- Score: {score.total} ({score.label})",
                f"- Reasons: {', '.join(score.reasons) if score.reasons else 'none'}",
                "",
            ]
        )
    return "\n".join(lines)


def _cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")
