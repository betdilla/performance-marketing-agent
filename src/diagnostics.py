from .metrics import f, pct_change, ratio

def diagnose_case(campaign, creative, cohort, target_cpa=40.0):
    conversions = int(float(campaign["conversions"]))
    cpa = f(campaign, "cpa")
    platform_roas = f(campaign, "platform_roas")
    backend_roas = f(cohort, "d30_backend_roas")
    ltv = f(cohort, "d90_ltv")
    repeat_rate = f(cohort, "repeat_rate")
    payback = f(cohort, "payback_days")
    ctr_delta = pct_change(f(creative, "ctr"), f(creative, "prev_ctr"))
    frequency_delta = pct_change(f(creative, "frequency"), f(creative, "prev_frequency"))
    funnel_delta = pct_change(f(cohort, "registration_to_conversion_rate"), f(cohort, "prev_registration_to_conversion_rate"))
    ltv_cpa = ratio(ltv, cpa)
    attribution_gap = platform_roas - backend_roas
    flags = []

    if conversions <= 3:
        flags.append("LOW_DATA_CONFIDENCE")
    if ctr_delta <= -0.20 and frequency_delta >= 0.30 and funnel_delta <= -0.10:
        flags.append("CREATIVE_FATIGUE_PATTERN")

    media_stable = abs(pct_change(f(campaign, "ctr"), f(campaign, "prev_ctr"))) <= 0.10
    landing_stable = abs(pct_change(f(campaign, "landing_cvr"), f(campaign, "prev_landing_cvr"))) <= 0.10
    if media_stable and landing_stable and funnel_delta <= -0.30:
        flags.append("DOWNSTREAM_FUNNEL_ANOMALY")
    if attribution_gap >= 0.50:
        flags.append("ATTRIBUTION_DISCREPANCY")
    if cpa <= target_cpa and (backend_roas < 0.90 or repeat_rate < 0.30 or ltv_cpa < 1.80):
        flags.append("CHEAP_CPA_WEAK_DOWNSTREAM")
    if cpa > target_cpa and backend_roas >= 1.0 and ltv_cpa >= 1.80 and payback <= 90:
        flags.append("HIGH_CPA_STRONG_COHORT")

    return {"case_id": campaign["case_id"], "conversions": conversions, "cpa": cpa, "platform_roas": platform_roas, "backend_roas": backend_roas, "ltv_cpa": round(ltv_cpa, 2), "repeat_rate": repeat_rate, "payback_days": payback, "ctr_change_pct": round(ctr_delta*100,1), "frequency_change_pct": round(frequency_delta*100,1), "downstream_conversion_change_pct": round(funnel_delta*100,1), "attribution_gap": round(attribution_gap,2), "flags": flags}
