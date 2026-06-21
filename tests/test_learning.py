from achievement_lab.learning import render_learning_log
from achievement_lab.models import Contribution


def test_render_learning_log_groups_contributions_by_kind() -> None:
    log = render_learning_log(
        [
            Contribution(
                "Review parser validation",
                "review",
                "Check parser validation behavior with malformed plans.",
                "Prevents unclear review feedback.",
                tests=["python -m pytest tests/test_cli.py -q"],
            ),
            Contribution(
                "Document export workflow",
                "docs",
                "Explain how to generate each report export format.",
                "Readers can reproduce the CLI workflow.",
                evidence=["README preview"],
            ),
        ],
        week="2026-W25",
    )

    assert "Week: 2026-W25" in log
    assert "- `docs`: 1" in log
    assert "- `review`: 1" in log
    assert "- Verified entries: 2/2" in log
    assert "- Complete: no" in log
    assert "Review parser validation" in log


def test_render_learning_log_notes_missing_verification() -> None:
    log = render_learning_log(
        [
            Contribution(
                "Thin commit",
                "commit",
                "Small summary",
                "Small impact",
            )
        ]
    )

    assert "Verification: none recorded" in log
