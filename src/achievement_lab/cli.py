from __future__ import annotations

import argparse
from pathlib import Path

from achievement_lab.loaders import load_contributions
from achievement_lab.reporting import render_markdown
from achievement_lab.summaries import render_terminal_summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Score planned GitHub contributions.")
    parser.add_argument("plan", type=Path, help="Path to a JSON contribution plan")
    parser.add_argument("--report", type=Path, help="Optional markdown report output path")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    contributions = load_contributions(args.plan)
    report = render_markdown(contributions)

    for line in render_terminal_summary(contributions):
        print(line)

    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(report, encoding="utf-8")
        print(f"wrote {args.report}")


if __name__ == "__main__":
    main()
