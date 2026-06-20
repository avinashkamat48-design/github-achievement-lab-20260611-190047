from __future__ import annotations

import argparse
import json
from pathlib import Path

from achievement_lab.exports import write_csv
from achievement_lab.filters import filter_by_min_score
from achievement_lab.loaders import load_contributions
from achievement_lab.reporting import render_markdown
from achievement_lab.schema import contribution_plan_schema
from achievement_lab.summaries import render_terminal_summary
from achievement_lab.validation import validate_contributions


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Score planned GitHub contributions.")
    parser.add_argument("plan", type=Path, help="Path to a JSON contribution plan")
    parser.add_argument("--csv", type=Path, help="Optional CSV score output path")
    parser.add_argument("--min-score", type=int, help="Only show contributions at or above this score")
    parser.add_argument("--report", type=Path, help="Optional markdown report output path")
    parser.add_argument("--schema", type=Path, help="Optional JSON schema output path")
    parser.add_argument("--strict", action="store_true", help="Exit with an error when validation issues are present")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    contributions = filter_by_min_score(load_contributions(args.plan), args.min_score)
    report = render_markdown(contributions)

    if args.schema:
        args.schema.parent.mkdir(parents=True, exist_ok=True)
        args.schema.write_text(json.dumps(contribution_plan_schema(), indent=2) + "\n", encoding="utf-8")
        print(f"wrote {args.schema}")
    if args.csv:
        write_csv(args.csv, contributions)
        print(f"wrote {args.csv}")

    for line in render_terminal_summary(contributions):
        print(line)

    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(report, encoding="utf-8")
        print(f"wrote {args.report}")
    issues = validate_contributions(contributions)
    if args.strict and issues:
        print(f"validation failed with {len(issues)} issue(s)")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
