from achievement_lab.filters import filter_by_min_score
from achievement_lab.models import Contribution


def test_filter_by_min_score_keeps_high_quality_entries() -> None:
    ready = Contribution(
        "Ready",
        "pull_request",
        "Summary with enough context for maintainers to review.",
        "Improves review quality.",
        tests=["pytest"],
        risks=["stricter checks"],
    )
    weak = Contribution("Weak", "commit", "Tiny", "")

    assert filter_by_min_score([ready, weak], 80) == [ready]


def test_filter_by_min_score_returns_original_entries_without_threshold() -> None:
    contribution = Contribution("A", "docs", "Summary with enough useful words here.", "Impact")

    assert filter_by_min_score([contribution], None) == [contribution]
