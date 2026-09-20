import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.diagnostics import diagnose_case


def campaign(case_id, conversions=100, cpa=35, platform_roas=1.2, ctr=2.0, prev_ctr=2.0, frequency=2.0, prev_frequency=2.0, landing_cvr=4.0, prev_landing_cvr=4.0):
    return {"case_id":case_id,"conversions":str(conversions),"cpa":str(cpa),"platform_roas":str(platform_roas),"ctr":str(ctr),"prev_ctr":str(prev_ctr),"frequency":str(frequency),"prev_frequency":str(prev_frequency),"landing_cvr":str(landing_cvr),"prev_landing_cvr":str(prev_landing_cvr)}


def creative(ctr=2.0, prev_ctr=2.0, frequency=2.0, prev_frequency=2.0):
    return {"ctr":str(ctr),"prev_ctr":str(prev_ctr),"frequency":str(frequency),"prev_frequency":str(prev_frequency)}


def cohort(backend_roas=1.1, ltv=70, repeat_rate=.35, payback=80, reg_cvr=.40, prev_reg_cvr=.40):
    return {"d30_backend_roas":str(backend_roas),"d90_ltv":str(ltv),"repeat_rate":str(repeat_rate),"payback_days":str(payback),"registration_to_conversion_rate":str(reg_cvr),"prev_registration_to_conversion_rate":str(prev_reg_cvr)}


class AdversarialDiagnosticsTest(unittest.TestCase):
    def test_frequency_alone_does_not_create_fatigue_flag(self):
        result=diagnose_case(campaign("H",cpa=48,frequency=4.5,prev_frequency=2.0),creative(ctr=2.0,prev_ctr=2.0,frequency=4.5,prev_frequency=2.0),cohort())
        self.assertNotIn("CREATIVE_FATIGUE_PATTERN",result["flags"])

    def test_good_cpa_without_good_downstream_is_not_clean(self):
        result=diagnose_case(campaign("G",cpa=25),creative(),cohort(backend_roas=.55,ltv=30,repeat_rate=.15,payback=150))
        self.assertIn("CHEAP_CPA_WEAK_DOWNSTREAM",result["flags"])

    def test_tracking_like_pattern_does_not_invent_creative_fatigue(self):
        result=diagnose_case(campaign("L",conversions=20,cpa=60),creative(ctr=2.0,prev_ctr=2.0,frequency=2.0,prev_frequency=2.0),cohort(backend_roas=1.1,ltv=100,repeat_rate=.4,payback=70))
        self.assertNotIn("CREATIVE_FATIGUE_PATTERN",result["flags"])

    def test_attribution_conflict_is_exposed(self):
        result=diagnose_case(campaign("N",platform_roas=2.2),creative(),cohort(backend_roas=.8,ltv=70))
        self.assertIn("ATTRIBUTION_DISCREPANCY",result["flags"])

    def test_tiny_sample_is_low_confidence_signal(self):
        result=diagnose_case(campaign("E2",conversions=2,cpa=18,platform_roas=3.0),creative(),cohort(backend_roas=2.0,ltv=100,repeat_rate=.5,payback=30))
        self.assertIn("LOW_DATA_CONFIDENCE",result["flags"])

    def test_missing_metric_fails_closed(self):
        bad=cohort()
        del bad["d90_ltv"]
        with self.assertRaises(ValueError):
            diagnose_case(campaign("I"),creative(),bad)


if __name__=="__main__":
    unittest.main()
