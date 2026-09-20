import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.evaluate_ai_output import evaluate


class AIOutputEvaluatorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.expected=json.loads((ROOT/"tests"/"expected_decisions.json").read_text())
        cls.passing=(ROOT/"tests"/"fixtures"/"passing_ai_review.md").read_text()

    def test_known_good_fixture_passes(self):
        result=evaluate(self.passing,self.expected)
        self.assertTrue(result["passed"],result["failures"])

    def test_forbidden_scale_fails_case_a(self):
        bad=self.passing.replace("## Case A\nOBSERVATION: CPA is cheap but downstream economics are weak.\nDIAGNOSIS: Weak downstream economics.\nEVIDENCE: Backend ROAS and repeat rate are weak.\nCONFIDENCE: HIGH\nDECISION: HOLD","## Case A\nOBSERVATION: CPA is cheap but downstream economics are weak.\nDIAGNOSIS: Weak downstream economics.\nEVIDENCE: Backend ROAS and repeat rate are weak.\nCONFIDENCE: HIGH\nDECISION: SCALE")
        result=evaluate(bad,self.expected)
        self.assertFalse(result["passed"])
        self.assertIn("A: forbidden decision: SCALE",result["failures"])

    def test_missing_required_field_fails(self):
        bad=self.passing.replace("VALIDATION: Recheck mature cohort.","")
        result=evaluate(bad,self.expected)
        self.assertFalse(result["passed"])
        self.assertTrue(any("missing fields" in x for x in result["failures"]))

    def test_bad_confidence_fails(self):
        bad=self.passing.replace("CONFIDENCE: LOW\nDECISION: TEST","CONFIDENCE: ABSOLUTE\nDECISION: TEST")
        result=evaluate(bad,self.expected)
        self.assertFalse(result["passed"])
        self.assertIn("E: confidence must be LOW, MEDIUM or HIGH",result["failures"])


if __name__=="__main__":
    unittest.main()
