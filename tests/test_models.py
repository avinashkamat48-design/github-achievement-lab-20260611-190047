from achievement_lab.models import Contribution


def test_contribution_requires_core_context_to_be_actionable() -> None:
    contribution = Contribution(title="Fix docs", kind="docs", summary="", impact="Clearer setup")

    assert not contribution.is_actionable()


def test_contribution_detects_verification_evidence() -> None:
    contribution = Contribution(
        title="Add parser test",
        kind="commit",
        summary="Add coverage for invalid parser input.",
        impact="Prevents regressions.",
        tests=["python -m pytest"],
    )

    assert contribution.has_verification()
