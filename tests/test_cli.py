from achievement_lab.cli import build_parser
import pytest


def test_cli_parser_accepts_plan_report_and_schema_paths() -> None:
    args = build_parser().parse_args(
        [
            "plan.json",
            "--csv",
            "scores.csv",
            "--html",
            "report.html",
            "--learning-log",
            "learning.md",
            "--min-score",
            "80",
            "--report",
            "out.md",
            "--schema",
            "schema.json",
            "--strict",
            "--week",
            "2026-W25",
        ]
    )

    assert args.plan.name == "plan.json"
    assert args.csv.name == "scores.csv"
    assert args.html.name == "report.html"
    assert args.learning_log.name == "learning.md"
    assert args.min_score == 80
    assert args.report.name == "out.md"
    assert args.schema.name == "schema.json"
    assert args.strict
    assert args.week == "2026-W25"


def test_cli_parser_accepts_template_generation_without_plan() -> None:
    args = build_parser().parse_args(["--template-kind", "docs", "--template-output", "docs-plan.json"])

    assert args.plan is None
    assert args.template_kind == "docs"
    assert args.template_output.name == "docs-plan.json"


@pytest.mark.parametrize("value", ["-1", "101", "high"])
def test_cli_parser_rejects_invalid_min_score(value: str) -> None:
    with pytest.raises(SystemExit):
        build_parser().parse_args(["plan.json", "--min-score", value])
