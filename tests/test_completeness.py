from achievement_lab.completeness import assess_completeness
from achievement_lab.models import Contribution


def test_assess_completeness_accepts_verified_risk_aware_entries() -> None:
    summary = assess_completeness(
        [
            Contribution(
                "Add parser tests",
                "commit",
                "Add tests for malformed contribution plans.",
                "Prevents confusing errors.",
                tests=["python -m pytest"],
                risks=["stricter parser behavior"],
            )
        ]
    )

    assert summary.is_complete
    assert summary.kinds == ("commit",)


def test_assess_completeness_detects_missing_risks_and_verification() -> None:
    summary = assess_completeness(
        [Contribution("Thin note", "docs", "Small summary", "Small impact")]
    )

    assert not summary.is_complete
    assert summary.verified == 0
    assert summary.with_risks == 0
