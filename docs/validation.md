# Validation

The lab validates contribution plans at two levels.

## Loader Validation

Loader validation rejects malformed input:

- The plan must be a JSON list.
- Each entry must be an object.
- `title`, `kind`, `summary`, and `impact` are required.
- `kind` must be one of the supported contribution kinds.

## Quality Validation

Quality validation flags weak but parseable entries:

- Short summaries
- Missing tests or evidence
- Pull requests and reviews without risk notes

Use `--strict` when you want validation issues to fail the command.
