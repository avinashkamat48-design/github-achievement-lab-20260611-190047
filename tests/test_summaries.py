from achievement_lab.models import Contribution
from achievement_lab.summaries import render_terminal_summary


def test_render_terminal_summary_includes_score_label_and_title() -> None:
    lines = render_terminal_summary(
        [
            Contribution(
                title="Document verification",
                kind="docs",
                summary="Explain the command used to verify a documentation change.",
                impact="Readers can repeat the check.",
                evidence=["README preview"],
            )
        ]
    )

    assert len(lines) == 1
    assert "Document verification" in lines[0]
