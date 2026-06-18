import json

import pytest

from achievement_lab.loaders import load_contributions


def test_load_contributions_reads_json_entries(tmp_path) -> None:
    path = tmp_path / "plan.json"
    path.write_text(
        json.dumps(
            [
                {
                    "title": "Add docs",
                    "kind": "docs",
                    "summary": "Explain how to verify a contribution.",
                    "impact": "Reviewers can reproduce the change.",
                }
            ]
        ),
        encoding="utf-8",
    )

    contributions = load_contributions(path)

    assert contributions[0].title == "Add docs"
    assert contributions[0].kind == "docs"


def test_load_contributions_rejects_non_list_json(tmp_path) -> None:
    path = tmp_path / "plan.json"
    path.write_text('{"title": "not a list"}', encoding="utf-8")

    with pytest.raises(ValueError, match="JSON list"):
        load_contributions(path)


def test_load_contributions_rejects_unknown_kind(tmp_path) -> None:
    path = tmp_path / "plan.json"
    path.write_text(
        json.dumps(
            [
                {
                    "title": "Mystery work",
                    "kind": "achievement",
                    "summary": "This kind is not supported.",
                    "impact": "The loader should reject it.",
                }
            ]
        ),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="unknown contribution kind"):
        load_contributions(path)
