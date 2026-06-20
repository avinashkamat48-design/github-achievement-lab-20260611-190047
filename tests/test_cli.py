from achievement_lab.cli import build_parser


def test_cli_parser_accepts_plan_report_and_schema_paths() -> None:
    args = build_parser().parse_args(
        [
            "plan.json",
            "--csv",
            "scores.csv",
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
    assert args.min_score == 80
    assert args.report.name == "out.md"
    assert args.schema.name == "schema.json"
    assert args.strict
