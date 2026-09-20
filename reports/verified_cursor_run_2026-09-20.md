# Verified Cursor Run

This artifact records the first end-to-end external Cursor Agent validation of the repository workflow.

## Run metadata

- Date: 2026-09-20
- Repository commit tested: `1dfd2203aa2cf1e7ce73bd4f4b48d94fe0be9969`
- Environment: local Cursor project on macOS
- Dataset: synthetic benchmark Cases A-F
- Mode: read-only
- Deterministic test suite: 25/25 passed locally
- AI output evaluator: PASS
- Evaluator failures: none

## AI decisions

| Case | Decision | Result |
| --- | --- | --- |
| A | HOLD | PASS |
| B | SCALE | PASS |
| C | TEST | PASS |
| D | FIX | PASS |
| E | TEST | PASS |
| F | FIX | PASS |

## Validation flow

`synthetic inputs -> deterministic diagnostics -> normalized evidence -> Cursor Agent + project rules -> structured recommendation -> machine evaluator -> PASS`

The Cursor Agent was instructed to inspect the repository rules and relevant project files, generate the complete daily review, remain read-only, and avoid changing the benchmark or evaluator to make the response pass.

The generated review was then evaluated with:

    python3 scripts/evaluate_ai_review.py reports/cursor_review.md

The evaluator returned:

    "passed": true
    "failures": []

This is evidence of one successful reproducible run, not a claim that every model or future run will always pass. The benchmark uses synthetic data and requires human approval before any real-world action.
