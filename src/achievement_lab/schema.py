from __future__ import annotations

from achievement_lab.models import CONTRIBUTION_KINDS


def contribution_plan_schema() -> dict:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "Contribution quality plan",
        "type": "array",
        "items": {
            "type": "object",
            "required": ["title", "kind", "summary", "impact"],
            "additionalProperties": False,
            "properties": {
                "title": {"type": "string", "minLength": 1},
                "kind": {"type": "string", "enum": sorted(CONTRIBUTION_KINDS)},
                "summary": {"type": "string", "minLength": 1},
                "impact": {"type": "string", "minLength": 1},
                "evidence": {"type": "array", "items": {"type": "string"}},
                "tests": {"type": "array", "items": {"type": "string"}},
                "risks": {"type": "array", "items": {"type": "string"}},
            },
        },
    }
