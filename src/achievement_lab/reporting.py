from __future__ import annotations

from achievement_lab.models import Contribution
from achievement_lab.recommendations import recommend_next_steps
from achievement_lab.scoring import score_contribution
from achievement_lab.summaries import summarize_by_kind, summarize_by_label
from achievement_lab.validation import validate_contributions


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

    lines.extend(["", "## Summary", ""])
    lines.append(f"- Contributions: {len(contributions)}")
    for kind, count in sorted(summarize_by_kind(contributions).items()):
        lines.append(f"- `{kind}`: {count}")
    for label, count in sorted(summarize_by_label(contributions).items()):
        lines.append(f"- `{label}`: {count}")

    lines.extend(["", "## Details", ""])
    for contribution in contributions:
        score = score_contribution(contribution)
        recommendations = recommend_next_steps(contribution)
        lines.extend(
            [
                f"### {contribution.title}",
                "",
                f"- Kind: `{contribution.kind}`",
                f"- Impact: {contribution.impact}",
                f"- Score: {score.total} ({score.label})",
                f"- Reasons: {', '.join(score.reasons) if score.reasons else 'none'}",
                f"- Next steps: {', '.join(recommendations) if recommendations else 'none'}",
                "",
            ]
        )
    issues = validate_contributions(contributions)
    lines.extend(["## Validation", ""])
    if not issues:
        lines.append("- No validation issues found.")
    else:
        for issue in issues:
            lines.append(f"- **{issue.severity}** `{issue.title}`: {issue.message}")
    return "\n".join(lines)


def _cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")
