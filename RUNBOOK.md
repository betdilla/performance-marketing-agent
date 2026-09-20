# Reviewer Runbook

This runbook is designed for an external reviewer starting from a clean clone.

## 1. Clone and verify the deterministic layer

    git clone https://github.com/betdilla/performance-marketing-agent.git
    cd performance-marketing-agent
    python3 scripts/prepare_review.py
    python3 -m unittest discover -s tests -v

The commands require Python 3.10+ and no third-party packages. The generated evidence report is `reports/normalized_review.md`.

## 2. Run the AI review in Cursor

Open the repository root as the Cursor project. The checked-in project rules are in `.cursor/rules/*.mdc` and use `alwaysApply: true`.

Start a new Agent chat and provide this instruction:

    Follow prompts/daily_review.md. Review all cases in reports/normalized_review.md using context/sample_client.md. Return the requested Case A-F report and portfolio summary. Do not modify advertising platforms or claim any action was executed.

Save the model response as a Markdown file, for example `reports/cursor_review.md`.

The repository does not commit a fabricated Cursor output. A reviewer should generate the output with the model available in their own Cursor session.

## 3. Evaluate the model response

    python3 scripts/evaluate_ai_review.py reports/cursor_review.md

Exit code 0 means the response passed the machine-readable decision contract in `tests/expected_decisions.json`. Exit code 1 means at least one benchmark guardrail failed.

The evaluator checks structure and selected benchmark concepts. Human review is still required for reasoning quality and causality.

## 4. Inspect the difficult cases

A: cheap CPA must not override weak downstream economics.
B: CPA above target must not automatically trigger STOP when cohort economics are strong.
C: the fatigue pattern is a working diagnosis, not proof of causality.
D: stable upstream plus downstream collapse requires investigation and `CAUSE NOT YET ESTABLISHED` when the root cause is unresolved.
E: three conversions are LOW DATA CONFIDENCE and must not trigger aggressive SCALE.
F: platform/backend disagreement must be reconciled before scaling from platform ROAS.

## Scope

The MVP is read-only. It contains no advertising-platform credentials and performs no campaign writes. The intended flow is evidence -> analysis -> recommendation -> human approval.
