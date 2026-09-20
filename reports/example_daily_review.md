# Example AI Daily Review

This report is an example of the expected AI recommendation layer after deterministic evidence preparation. The inputs are synthetic.

## Case A

OBSERVATION: CPA is below target, but downstream economics are weak.

DIAGNOSIS: Acquisition is efficient at the conversion event, but current cohort quality does not support scaling.

EVIDENCE: CPA $31 vs $40 target; backend D30 ROAS 0.61; repeat rate 18%; D90 LTV/CPA 1.35.

CONFIDENCE: HIGH

DECISION: HOLD

ACTION: Maintain current exposure and segment downstream quality by acquisition dimension before adding budget.

EXPECTED IMPACT: Avoid scaling cheap conversions that currently fail business-economics thresholds while preserving diagnostic volume.

RISK: Later cohort maturation could improve the economics.

VALIDATION: Reassess at the next cohort maturity checkpoint and require improving backend ROAS, repeat behavior and LTV/CPA before SCALE.

## Case B

OBSERVATION: CPA is $43, above the nominal $40 target, while downstream economics exceed commercial thresholds.

DIAGNOSIS: The nominal CPA target understates the observed value of this cohort.

EVIDENCE: Backend D30 ROAS 1.18; D90 LTV/CPA 2.14; repeat rate 44%; payback 74 days.

CONFIDENCE: HIGH

DECISION: SCALE

ACTION: Run a controlled budget expansion and compare the incremental cohort with the current cohort.

EXPECTED IMPACT: Capture additional economically supported volume while measuring marginal quality.

RISK: Cohort economics can deteriorate as spend expands.

VALIDATION: Require incremental payback <= 90 days and D90 LTV/CPA >= 1.80.

## Case C

OBSERVATION: CTR fell materially while frequency rose and downstream conversion deteriorated.

DIAGNOSIS: CREATIVE FATIGUE is a supported working diagnosis, not proven causality.

EVIDENCE: CTR change -47.6%; frequency change +84.6%; registration-to-conversion change -16.3%.

CONFIDENCE: MEDIUM

DECISION: TEST

ACTION: Introduce fresh creative concepts/variations while keeping other controllable conditions as stable as practical.

EXPECTED IMPACT: Determine whether creative refresh restores engagement and conversion efficiency.

RISK: Audience saturation or another correlated factor may also contribute.

VALIDATION: Compare refreshed cells against the fatigued cell for CTR recovery and downstream conversion improvement.

## Case D

OBSERVATION: Upstream engagement and landing conversion are stable, while registration-to-conversion fell sharply.

DIAGNOSIS: CAUSE NOT YET ESTABLISHED. Evidence localizes the anomaly downstream of registration rather than establishing a media-delivery cause.

EVIDENCE: CTR and landing CVR remain near prior levels; registration-to-conversion change is approximately -51%.

CONFIDENCE: HIGH

DECISION: FIX

ACTION: Audit post-registration funnel, product/payment availability and tracking integrity before making acquisition cuts.

EXPECTED IMPACT: Isolate or repair the downstream break without discarding otherwise stable acquisition traffic.

RISK: A hidden traffic-quality shift could still exist despite stable surface metrics.

VALIDATION: Reconcile post-registration events with backend records and inspect stage-level conversion after registration.

## Case E

OBSERVATION: Apparent CPA and ROAS are strong, but the result is based on only 3 conversions.

DIAGNOSIS: CAUSE NOT YET ESTABLISHED. The sample is insufficient to establish scalable economics.

EVIDENCE: 3 conversions; CPA $24; platform ROAS 2.40; backend D30 ROAS 1.90.

CONFIDENCE: LOW

DECISION: TEST

ACTION: Continue only within a bounded learning budget to accumulate a decision-quality sample.

EXPECTED IMPACT: Reduce the chance of scaling statistical noise while preserving learning.

RISK: Early economics may regress materially as the sample grows.

VALIDATION: Re-evaluate after materially more conversions and sufficient cohort maturity.

## Case F

OBSERVATION: Platform and backend ROAS materially disagree.

DIAGNOSIS: Attribution/data discrepancy requires validation before commercial scaling.

EVIDENCE: Platform ROAS 2.10 vs backend D30 ROAS 0.76, a 1.34 absolute gap.

CONFIDENCE: HIGH

DECISION: FIX

ACTION: Reconcile attribution windows, event deduplication and backend revenue mapping before using platform ROAS for expansion.

EXPECTED IMPACT: Restore a trustworthy economic signal for allocation decisions.

RISK: If the backend feed is faulty, conservative allocation may temporarily constrain valid volume.

VALIDATION: Reconcile sampled conversions and revenue across platform and backend and confirm the gap falls within an accepted tolerance.

## Portfolio summary

Highest-priority exceptions are the downstream break in D and attribution conflict in F. A should be held despite cheap acquisition because cohort economics are weak. B supports a controlled scale test despite CPA above target. C needs a creative-refresh experiment. E remains exploratory because sample size is insufficient.
