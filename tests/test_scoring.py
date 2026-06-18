from achievement_lab.models import Contribution
from achievement_lab.scoring import score_contribution


def test_ready_score_needs_context_verification_and_risk_awareness() -> None:
    contribution = Contribution(
        title="Validate input data",
        kind="pull_request",
        summary="Reject malformed contribution plan input before generating a report.",
        impact="Users get actionable failures instead of a stack trace.",
        evidence=["manual bad JSON fixture"],
        tests=["python -m pytest"],
        risks=["stricter validation may reject old examples"],
    )

    score = score_contribution(contribution)

    assert score.label == "ready"
    assert score.total >= 80


def test_low_context_activity_is_not_ready() -> None:
    contribution = Contribution(title="Update", kind="commit", summary="Stuff", impact="")

    score = score_contribution(contribution)

    assert score.label == "not ready"
