"""Naïve CSV → JSON Lines converter.

INTENTIONAL LIMITATIONS (candidates will fix):
* Does **no** visit_id deduplication
* Accepts any date string, does not coerce ISO‑8601
* Treats missing cost as 0 instead of null (None)
"""
import csv, json
from typing import List

def csv_to_json_lines(csv_path: str) -> str:
    """Return the CSV file converted to JSONL string."""
    rows: List[str] = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # naive mapping
            visit = {
                "visit_id": row["visit_id"],
                "visit_date": row["visit_date"],  # no validation
                "cost": float(row["cost"]) if row["cost"] else 0.0
            }
            rows.append(json.dumps(visit, separators=(',', ':')))
    return "\n".join(rows)
