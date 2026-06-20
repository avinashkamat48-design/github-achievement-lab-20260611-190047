# Exports

The CLI can produce multiple review artifacts from the same JSON plan.

## Markdown

Use `--report reports/quality-report.md` for a GitHub-friendly summary.

## CSV

Use `--csv reports/quality-report.csv` when you want to inspect scores in a
spreadsheet.

## HTML

Use `--html reports/quality-report.html` for a browser-readable report.

## JSON Schema

Use `--schema reports/contribution-plan.schema.json` to generate a schema for
editor integration or CI validation.
