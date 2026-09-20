import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.diagnostics import diagnose_case
from src.load_data import index_by_case, load_csv

class BenchmarkDiagnosticsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.campaigns=index_by_case(load_csv(ROOT/"data"/"sample_campaigns.csv"))
        cls.creatives=index_by_case(load_csv(ROOT/"data"/"sample_creatives.csv"))
        cls.cohorts=index_by_case(load_csv(ROOT/"data"/"sample_cohorts.csv"))

    def result(self, cid):
        return diagnose_case(self.campaigns[cid], self.creatives[cid], self.cohorts[cid])

    def assert_flag(self,cid,flag):
        self.assertIn(flag,self.result(cid)["flags"])

    def test_a(self): self.assert_flag("A","CHEAP_CPA_WEAK_DOWNSTREAM")
    def test_b(self): self.assert_flag("B","HIGH_CPA_STRONG_COHORT")
    def test_c(self): self.assert_flag("C","CREATIVE_FATIGUE_PATTERN")
    def test_d(self): self.assert_flag("D","DOWNSTREAM_FUNNEL_ANOMALY")
    def test_e(self): self.assert_flag("E","LOW_DATA_CONFIDENCE")
    def test_f(self): self.assert_flag("F","ATTRIBUTION_DISCREPANCY")

if __name__=="__main__":
    unittest.main()
