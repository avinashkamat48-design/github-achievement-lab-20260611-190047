# GitHub Achievement Lab

A small public practice repo for learning GitHub issues, pull requests, code review,
and contribution workflows without turning the contribution graph into noise.

The repo now doubles as a lightweight contribution-quality kit: it collects
repeatable checklists, scoring helpers, and examples for deciding whether a
GitHub activity is useful enough to publish.

## What This Repo Is For

- Practicing scoped commits and pull requests
- Keeping issue comments useful and specific
- Writing code reviews that point to concrete behavior
- Tracking learning notes from open-source work
- Separating real contribution work from graph-padding habits

## Quick Links

- [Workflow notes](docs/workflow.md)
- [Pull request checklist](docs/pr-checklist.md)
- [Review notes](docs/review-notes.md)
- [Learning log](docs/learning-log.md)
- [Learning log completeness](docs/completeness.md)
- [Learning log export](docs/learning-log-export.md)
- [Validation](docs/validation.md)
- [Exports](docs/exports.md)
- [Example plans](docs/examples.md)
- [Contribution plan templates](docs/templates.md)
- [Safe public examples](docs/safe-examples.md)

## Local Usage

```bash
python -m pytest -q
python -m achievement_lab.cli examples/quality-plan.json \
  --report reports/quality-report.md \
  --csv reports/quality-report.csv \
  --html reports/quality-report.html \
  --learning-log reports/weekly-learning-log.md \
  --schema reports/contribution-plan.schema.json
```

The CLI scores each planned contribution and writes a Markdown report that is
easy to skim before opening a pull request, issue, or review.
