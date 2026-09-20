# Performance Marketing AI Agent

A reproducible, read-only workflow for diagnosing performance marketing data and producing evidence-based recommendations.

This project formalizes part of a performance marketing methodology into an AI-assisted review workflow. It is an MVP for analysis and recommendation, not an autonomous media-buying system.

## What it does

The workflow combines campaign, creative, cohort and client-economics inputs. It prioritizes business outcomes over surface media metrics and returns SCALE, HOLD, TEST, FIX or STOP.

Every recommendation must include observation, diagnosis, evidence, confidence, action, expected impact, risk and a validation point.

## Architecture

synthetic inputs -> deterministic Python checks -> normalized evidence -> AI analysis + project rules -> recommendation -> human approval

Python owns calculations and anomaly flags. The AI layer owns diagnosis, conflicting-signal reasoning and recommended next actions. The MVP has no advertising-platform write access.

## Inputs

- data/sample_campaigns.csv: delivery and acquisition metrics
- data/sample_creatives.csv: creative performance and fatigue signals
- data/sample_cohorts.csv: backend revenue, repeat behavior and attribution
- context/sample_client.md: targets and business constraints

All included data is synthetic and anonymized.

## How to run

Requires Python 3.10+.

    python3 scripts/prepare_review.py
    python3 -m unittest discover -s tests -v

The first command writes reports/normalized_review.md. Open this repository in Cursor and use prompts/daily_review.md to analyze that evidence under the project rules in .cursor/rules/.

No API key is required for the deterministic layer.

## Decision framework

Reasoning priority: Business profitability -> Cohort quality -> LTV/payback/backend ROAS -> CAC/CPA -> Funnel conversion -> Media efficiency -> Delivery metrics.

A good CPA is not sufficient evidence to scale. A CPA above target is not sufficient evidence to stop. Backend economics can override platform attribution.

## Benchmark scenarios

The synthetic fixture contains six deliberately ambiguous cases: A good CPA with weak downstream economics; B CPA above target with strong LTV/payback; C creative fatigue; D downstream conversion break despite stable media; E excellent apparent performance on only three conversions; F platform/backend attribution conflict.

## Limitations

This MVP uses synthetic data, simplified cohort windows and heuristic anomaly flags. Recommendations require human review. The deterministic layer does not claim causal identification, and the AI layer is instructed to state CAUSE NOT YET ESTABLISHED when evidence is insufficient.

## Safety and guardrails

Read-only by design. No platform write access. No credentials or confidential client data. No invented metrics or causal claims. Low sample sizes reduce confidence. Attribution conflicts are surfaced rather than silently resolved. Human approval remains the final gate.

## Future API integration

A later version can ingest platform and backend APIs into a normalization layer, produce recommendations, pass them through explicit guardrails and request human approval before any API action. Write access is intentionally outside this MVP.

## Background

The repository is a recent formalization of performance-marketing methodology into a reproducible AI analysis workflow. It should not be interpreted as a claim that this agent historically operated advertising budgets. Historical automation experience and this AI workflow are separate.
