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
    assert "## Summary" in report
    assert "- Contributions: 1" in report
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


def test_render_markdown_includes_validation_issues() -> None:
    report = render_markdown(
        [
            Contribution(
                title="Thin update",
                kind="commit",
                summary="Small note",
                impact="Tiny",
            )
        ]
    )

    assert "## Validation" in report
    assert "missing evidence or tests" in report
    assert "Next steps:" in report
