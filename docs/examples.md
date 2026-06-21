# Example Plans

The `examples/` directory contains plans for different learning cases.

## `quality-plan.json`

A high-quality plan with verification, risks, and clear impact.

## `triage-plan.json`

A focused issue-triage plan that demonstrates reproducible evidence.

## `docs-plan.json`

A docs-focused plan that shows how documentation work can still include
evidence, verification, and risk notes.

## `review-plan.json`

A review-focused plan that demonstrates how an actionable review finding can
include code-path evidence, verification, and reviewer assumptions.

## `weak-plan.json`

A deliberately weak plan. Use it with `--strict` to see validation failures:

```bash
python -m achievement_lab.cli examples/weak-plan.json --strict
```
