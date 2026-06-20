from achievement_lab.models import Contribution
from achievement_lab.summaries import render_terminal_summary, summarize_by_kind, summarize_by_label


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


def test_summarize_by_kind_counts_contribution_types() -> None:
    contributions = [
        Contribution("A", "commit", "Summary with enough useful words here.", "Impact", tests=["pytest"]),
        Contribution("B", "docs", "Summary with enough useful words here.", "Impact", evidence=["preview"]),
    ]

    assert summarize_by_kind(contributions) == {"commit": 1, "docs": 1}


def test_summarize_by_label_counts_readiness_labels() -> None:
    contributions = [
        Contribution("A", "commit", "Summary with enough useful words here.", "Impact", tests=["pytest"]),
        Contribution("B", "commit", "Tiny", ""),
    ]

    labels = summarize_by_label(contributions)

    assert labels["needs polish"] == 1
    assert labels["not ready"] == 1
