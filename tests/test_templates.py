import pytest

from achievement_lab.templates import template_for, template_kinds


def test_template_for_returns_supported_kind() -> None:
    template = template_for("review")

    assert template["kind"] == "review"
    assert template["title"]
    assert template["risks"]


def test_template_for_returns_independent_copies() -> None:
    first = template_for("commit")
    second = template_for("commit")
    first["tests"].append("extra")

    assert "extra" not in second["tests"]


def test_template_kinds_lists_all_templates() -> None:
    assert "pull_request" in template_kinds()
    assert "docs" in template_kinds()


def test_template_for_rejects_unknown_kind() -> None:
    with pytest.raises(ValueError, match="unknown contribution kind"):
        template_for("badge")
