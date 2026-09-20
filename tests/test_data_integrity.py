import csv
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def read(name):
    with (ROOT/"data"/name).open(newline="",encoding="utf-8") as f:
        return list(csv.DictReader(f))


class DataIntegrityTest(unittest.TestCase):
    def test_case_ids_match_across_inputs(self):
        sets=[{r["case_id"] for r in read(n)} for n in ("sample_campaigns.csv","sample_creatives.csv","sample_cohorts.csv")]
        self.assertEqual(sets[0],sets[1])
        self.assertEqual(sets[1],sets[2])
        self.assertEqual(sets[0],set("ABCDEF"))

    def test_no_blank_cells(self):
        for name in ("sample_campaigns.csv","sample_creatives.csv","sample_cohorts.csv"):
            for row in read(name):
                self.assertTrue(all(v not in ("",None) for v in row.values()),name+" contains blank data")


if __name__=="__main__":
    unittest.main()
