from achievement_lab.models import Contribution
from achievement_lab.validation import validate_contributions


def test_validate_contributions_flags_missing_verification() -> None:
    contribution = Contribution(
        title="Review parser change",
        kind="review",
        summary="Check whether the parser handles malformed contribution plans clearly.",
        impact="Maintainers get clearer feedback.",
        risks=["review may miss context from a linked issue"],
    )

    issues = validate_contributions([contribution])

    assert any(issue.severity == "error" and "verification" in issue.message for issue in issues)


def test_validate_contributions_accepts_well_supported_plan() -> None:
    contribution = Contribution(
        title="Add report test",
        kind="commit",
        summary="Add regression coverage for rendering Markdown contribution reports.",
        impact="Report output stays stable.",
        tests=["python -m pytest tests/test_reporting.py -q"],
    )

    assert validate_contributions([contribution]) == []
