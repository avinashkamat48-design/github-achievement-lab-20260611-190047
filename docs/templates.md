# Contribution Plan Templates

Use templates when you want a public-safe starter plan for a specific
contribution kind.

## Generate a Template

```bash
python -m achievement_lab.cli \
  --template-kind review \
  --template-output examples/generated-review-plan.json
```

Supported template kinds:

- `commit`
- `pull_request`
- `issue`
- `review`
- `docs`

Templates are intentionally not perfect final plans. Replace placeholder text
with the actual impact, verification, and risk notes before publishing work.
