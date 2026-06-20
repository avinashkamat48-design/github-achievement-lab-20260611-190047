# Example Plans

The `examples/` directory contains plans for different learning cases.

## `quality-plan.json`

A high-quality plan with verification, risks, and clear impact.

## `triage-plan.json`

A focused issue-triage plan that demonstrates reproducible evidence.

## `weak-plan.json`

A deliberately weak plan. Use it with `--strict` to see validation failures:

```bash
python -m achievement_lab.cli examples/weak-plan.json --strict
```
