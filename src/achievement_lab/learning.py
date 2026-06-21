from __future__ import annotations

from collections import defaultdict

from achievement_lab.completeness import assess_completeness
from achievement_lab.models import Contribution
from achievement_lab.scoring import score_contribution


def render_learning_log(contributions: list[Contribution], *, week: str = "current week") -> str:
    grouped: dict[str, list[Contribution]] = defaultdict(list)
    for contribution in contributions:
        grouped[contribution.kind].append(contribution)
    completeness = assess_completeness(contributions)

    lines = [
        "# Weekly Contribution Learning Log",
        "",
        f"Week: {week}",
        "",
        "## Summary",
        "",
        f"- Planned contributions: {len(contributions)}",
    ]

    for kind, items in sorted(grouped.items()):
        lines.append(f"- `{kind}`: {len(items)}")
    lines.extend(
        [
            f"- Verified entries: {completeness.verified}/{completeness.total}",
            f"- Entries with risk notes: {completeness.with_risks}/{completeness.total}",
            f"- Complete: {'yes' if completeness.is_complete else 'no'}",
        ]
    )

    lines.extend(["", "## Notes", ""])
    for kind, items in sorted(grouped.items()):
        lines.extend([f"### {kind}", ""])
        for contribution in items:
            score = score_contribution(contribution)
            lines.extend(
                [
                    f"- **{contribution.title}**",
                    f"  - Score: {score.total} ({score.label})",
                    f"  - Impact: {contribution.impact}",
                    f"  - Verification: {_verification(contribution)}",
                ]
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _verification(contribution: Contribution) -> str:
    checks = contribution.tests or contribution.evidence
    return "; ".join(checks) if checks else "none recorded"
