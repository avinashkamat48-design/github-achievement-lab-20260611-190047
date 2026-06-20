from achievement_lab.models import Contribution
from achievement_lab.recommendations import recommend_next_steps


def test_recommend_next_steps_flags_missing_verification() -> None:
    contribution = Contribution(
        title="Review change",
        kind="review",
        summary="Check whether the router behavior is safe.",
        impact="Avoids a regression.",
    )

    steps = recommend_next_steps(contribution)

    assert any("evidence" in step for step in steps)
    assert any("risk" in step for step in steps)


def test_recommend_next_steps_accepts_complete_contribution() -> None:
    contribution = Contribution(
        title="Add report test",
        kind="commit",
        summary="Add coverage for the report rendering path.",
        impact="Protects generated output.",
        tests=["python -m pytest"],
    )

    assert recommend_next_steps(contribution) == []
