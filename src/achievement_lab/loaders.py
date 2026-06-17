from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from achievement_lab.models import Contribution


def load_contributions(path: Path) -> list[Contribution]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("contribution file must contain a JSON list")
    return [_from_dict(item) for item in data]


def _from_dict(item: Any) -> Contribution:
    if not isinstance(item, dict):
        raise ValueError("each contribution entry must be an object")
    return Contribution(
        title=str(item.get("title", "")),
        kind=item.get("kind", "commit"),
        summary=str(item.get("summary", "")),
        impact=str(item.get("impact", "")),
        evidence=[str(value) for value in item.get("evidence", [])],
        tests=[str(value) for value in item.get("tests", [])],
        risks=[str(value) for value in item.get("risks", [])],
    )
