import csv
from pathlib import Path

def load_csv(path: Path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))

def index_by_case(rows):
    return {row["case_id"]: row for row in rows}
