from achievement_lab.exports import write_csv
from achievement_lab.models import Contribution


def test_write_csv_includes_scores(tmp_path) -> None:
    path = tmp_path / "scores.csv"
    write_csv(
        path,
        [
            Contribution(
                title="Add tests",
                kind="commit",
                summary="Add coverage for CSV export behavior.",
                impact="Spreadsheet output stays reliable.",
                tests=["python -m pytest"],
            )
        ],
    )

    content = path.read_text(encoding="utf-8")

    assert "title,kind,score,label,impact" in content
    assert "Add tests" in content
