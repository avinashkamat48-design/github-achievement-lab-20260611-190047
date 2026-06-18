# Architecture

The lab is intentionally small. It has three layers:

1. `models.py` defines contribution records.
2. `scoring.py` evaluates whether a contribution has enough context, impact,
   verification, and risk awareness.
3. `reporting.py` turns the score results into Markdown that can be reviewed
   before publishing work on GitHub.

The CLI in `cli.py` only coordinates loading, scoring, and report writing. It
does not call GitHub APIs or mutate repositories.
