from achievement_lab.cli import build_parser


def test_cli_parser_accepts_plan_and_report_paths() -> None:
    args = build_parser().parse_args(["plan.json", "--report", "out.md", "--strict"])

    assert args.plan.name == "plan.json"
    assert args.report.name == "out.md"
    assert args.strict
