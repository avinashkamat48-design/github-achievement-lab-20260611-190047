from __future__ import annotations

from copy import deepcopy

from achievement_lab.models import CONTRIBUTION_KINDS


_TEMPLATES: dict[str, dict] = {
    "commit": {
        "title": "Describe the focused code change",
        "kind": "commit",
        "summary": "Explain the behavior, test, or docs gap addressed by this commit.",
        "impact": "Describe who benefits from this change.",
        "evidence": [],
        "tests": ["python -m pytest -q"],
        "risks": ["Name compatibility or maintenance risk, or explain why risk is low."],
    },
    "pull_request": {
        "title": "Describe the reviewable pull request scope",
        "kind": "pull_request",
        "summary": "Explain the issue, implementation approach, and verification path.",
        "impact": "Describe how maintainers or users benefit.",
        "evidence": ["Link issue, reproduction, or before/after behavior."],
        "tests": ["List exact commands run."],
        "risks": ["Name rollout, compatibility, or review risks."],
    },
    "issue": {
        "title": "Describe the reproducible issue or docs gap",
        "kind": "issue",
        "summary": "Explain what happens, what was expected, and where it occurs.",
        "impact": "Describe why fixing or clarifying this helps.",
        "evidence": ["Add reproduction steps or observed output."],
        "tests": [],
        "risks": ["Mention uncertainty or environment-specific assumptions."],
    },
    "review": {
        "title": "Describe the actionable review finding",
        "kind": "review",
        "summary": "Explain the specific code path, consequence, and suggested fix.",
        "impact": "Describe what bug, regression, or maintenance risk is avoided.",
        "evidence": ["Reference changed file, line, or failing scenario."],
        "tests": ["Name the relevant check or missing test."],
        "risks": ["Mention any assumption behind the review comment."],
    },
    "docs": {
        "title": "Describe the documentation improvement",
        "kind": "docs",
        "summary": "Explain what reader confusion or missing workflow is addressed.",
        "impact": "Describe what the reader can do after the docs improve.",
        "evidence": ["Link preview, section, or command output."],
        "tests": ["Run or preview the documented command."],
        "risks": ["Note if docs depend on changing CLI behavior."],
    },
}


def template_for(kind: str) -> dict:
    if kind not in CONTRIBUTION_KINDS:
        allowed = ", ".join(sorted(CONTRIBUTION_KINDS))
        raise ValueError(f"unknown contribution kind '{kind}'; expected one of: {allowed}")
    return deepcopy(_TEMPLATES[kind])


def template_kinds() -> list[str]:
    return sorted(_TEMPLATES)
