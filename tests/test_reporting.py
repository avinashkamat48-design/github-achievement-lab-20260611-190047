from achievement_lab.models import Contribution
from achievement_lab.reporting import render_markdown


def test_render_markdown_includes_summary_table() -> None:
    report = render_markdown(
        [
            Contribution(
                title="Improve docs",
                kind="docs",
                summary="Add verification notes to the docs.",
                impact="Readers can reproduce the workflow.",
            )
        ]
    )

    assert "| Title | Kind | Score | Label |" in report
    assert "Improve docs" in report


def test_render_markdown_escapes_table_pipes() -> None:
    report = render_markdown(
        [
            Contribution(
                title="Fix parser | loader",
                kind="commit",
                summary="Keep Markdown tables valid when titles contain pipes.",
                impact="Reports stay readable.",
            )
        ]
    )

    assert "Fix parser \\| loader" in report
