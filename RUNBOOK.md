# External reviewer runbook

## 1. Clone

    git clone https://github.com/betdilla/performance-marketing-agent.git
    cd performance-marketing-agent

## 2. Verify deterministic layer

No package installation is required.

    python3 scripts/prepare_review.py
    python3 -m unittest discover -s tests -v

Expected result: all deterministic benchmark, adversarial and data-integrity tests pass.

## 3. Inspect the evidence

Open reports/normalized_review.md after running the preparation script.

The report contains calculated evidence and heuristic investigation flags. A flag is not a causal conclusion.

## 4. Run the AI review in Cursor

Open the repository as a project in Cursor. The project-level instruction layer is under .cursor/rules/.

Ask the agent to follow prompts/daily_review.md using:
- context/sample_client.md
- reports/normalized_review.md

The expected format is documented in reports/example_daily_review.md.

## 5. Review the traps

Compare the AI output with tests/benchmark_cases.md and tests/adversarial_cases.md.

The key test is not whether the model repeats labels. It is whether it handles conflicting signals correctly, refuses false precision, identifies insufficient evidence and remains read-only.

## Scope

This MVP produces recommendations only. It does not connect to or modify advertising accounts.
