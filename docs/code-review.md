# Code Review Guide

Good review comments are specific, testable, and tied to user-visible behavior
or maintainability risk.

## Review Comment Shape

1. Name the concrete problem.
2. Point to the code path or input that triggers it.
3. Explain the consequence.
4. Suggest the smallest fix or test.

## Strong Signals

- The finding can be reproduced.
- The comment includes file or line context.
- The reviewer distinguishes blocker, suggestion, and question.
- The review avoids style-only comments unless the repo has a written rule.
