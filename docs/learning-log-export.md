# Learning Log Export

The weekly learning-log export turns a contribution plan into a short reflection
artifact. It is useful after a batch of commits, reviews, issues, or pull
requests because it records what was practiced and how each item was verified.

## Usage

```bash
python -m achievement_lab.cli examples/quality-plan.json \
  --learning-log reports/weekly-learning-log.md \
  --week 2026-W25
```

## Contents

The generated log includes:

- A week label
- Contribution counts by kind
- Score and readiness label for each item
- Impact notes
- Verification commands or evidence
