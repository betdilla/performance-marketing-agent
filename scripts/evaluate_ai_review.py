import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.evaluate_ai_output import evaluate, load_expected


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 scripts/evaluate_ai_review.py <ai-review.md>")

    review_path = Path(sys.argv[1])
    if not review_path.is_absolute():
        review_path = ROOT / review_path

    expected = load_expected(ROOT / "tests" / "expected_decisions.json")
    result = evaluate(review_path.read_text(encoding="utf-8"), expected)
    print(json.dumps(result, indent=2))

    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
