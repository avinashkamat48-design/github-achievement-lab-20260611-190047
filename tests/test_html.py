from achievement_lab.html import render_html
from achievement_lab.models import Contribution


def test_render_html_outputs_table() -> None:
    html = render_html(
        [
            Contribution(
                title="Add HTML report",
                kind="commit",
                summary="Render contribution plan scores as an HTML table.",
                impact="Reports can be opened in a browser.",
                tests=["python -m pytest tests/test_html.py -q"],
            )
        ]
    )

    assert "<table>" in html
    assert "Next steps" in html
    assert "Add HTML report" in html


def test_render_html_escapes_titles() -> None:
    html = render_html([Contribution("<script>", "docs", "Summary with useful words here.", "Impact")])

    assert "&lt;script&gt;" in html
