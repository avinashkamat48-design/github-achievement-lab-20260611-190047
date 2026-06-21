# CLI Reference

```bash
python -m achievement_lab.cli PLAN [options]
```

## Arguments

- `PLAN`: path to a JSON contribution plan.

## Options

- `--report PATH`: write a Markdown quality report.
- `--csv PATH`: write a CSV score table.
- `--html PATH`: write an HTML quality report.
- `--learning-log PATH`: write a weekly learning-log Markdown file.
- `--schema PATH`: write the contribution plan JSON schema.
- `--min-score N`: only include contributions with score `N` or higher.
- `--strict`: return a non-zero exit code when validation finds issues.
- `--week TEXT`: label to use in the weekly learning log.

## Example

```bash
python -m achievement_lab.cli examples/quality-plan.json \
  --report reports/quality-report.md \
  --csv reports/quality-report.csv \
  --html reports/quality-report.html \
  --learning-log reports/weekly-learning-log.md \
  --schema reports/contribution-plan.schema.json \
  --week 2026-W25 \
  --strict
```
