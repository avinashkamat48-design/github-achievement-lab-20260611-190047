from achievement_lab.schema import contribution_plan_schema


def test_contribution_plan_schema_requires_core_fields() -> None:
    schema = contribution_plan_schema()

    assert schema["type"] == "array"
    assert schema["items"]["required"] == ["title", "kind", "summary", "impact"]
    assert "pull_request" in schema["items"]["properties"]["kind"]["enum"]
