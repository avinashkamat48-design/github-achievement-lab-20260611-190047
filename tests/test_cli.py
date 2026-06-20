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
            "--min-score",
            "80",
            "--report",
            "out.md",
            "--schema",
            "schema.json",
            "--strict",
        ]
    )

    assert args.plan.name == "plan.json"
    assert args.csv.name == "scores.csv"
    assert args.html.name == "report.html"
    assert args.min_score == 80
    assert args.report.name == "out.md"
    assert args.schema.name == "schema.json"
    assert args.strict


@pytest.mark.parametrize("value", ["-1", "101", "high"])
def test_cli_parser_rejects_invalid_min_score(value: str) -> None:
    with pytest.raises(SystemExit):
        build_parser().parse_args(["plan.json", "--min-score", value])
