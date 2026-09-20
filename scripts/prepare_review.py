import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.diagnostics import diagnose_case
from src.load_data import index_by_case, load_csv
from src.report import render_review

def main():
    campaigns = index_by_case(load_csv(ROOT / "data" / "sample_campaigns.csv"))
    creatives = index_by_case(load_csv(ROOT / "data" / "sample_creatives.csv"))
    cohorts = index_by_case(load_csv(ROOT / "data" / "sample_cohorts.csv"))
    case_ids = sorted(set(campaigns) & set(creatives) & set(cohorts))
    if not case_ids:
        raise RuntimeError("No shared case IDs")
    results = [diagnose_case(campaigns[c], creatives[c], cohorts[c]) for c in case_ids]
    output = render_review(results)
    path = ROOT / "reports" / "normalized_review.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(output, encoding="utf-8")
    print(output)
    print("\nWrote " + str(path.relative_to(ROOT)))

if __name__ == "__main__":
    main()
