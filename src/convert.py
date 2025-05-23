"""Naïve CSV → JSON Lines converter.

INTENTIONAL LIMITATIONS (candidates will fix):
* Does **no** visit_id deduplication
* Accepts any date string, does not coerce ISO-8601
* Treats missing cost as 0 instead of null (None)
"""

import csv
import json
import re
from typing import List

ISO_8601_REGEX = re.compile(
    r"^\d{4}-\d{2}-\d{2}"  # Date part
    r"(T\d{2}:\d{2}:\d{2}(\.\d{1,6})?(Z|[+-]\d{2}:\d{2})?)?$"  # Optional part
)


def _is_iso8601(date_str: str) -> bool:
    """Check if the date string is in ISO-8601 format."""
    return bool(ISO_8601_REGEX.fullmatch(date_str))


def csv_to_json_lines(csv_path: str) -> str:
    """Return the CSV file converted to JSONL string."""
    rows: List[str] = []
    seen_ids = set()
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            visit_id = row["visit_id"]
            visit_date = row["visit_date"]

            # Check duplicate visit_id
            if visit_id in seen_ids:
                raise ValueError(f"Duplicate visit_id found: {visit_id}")
            seen_ids.add(visit_id)

            # Check for ISO-8601 date format
            if not _is_iso8601(visit_date):
                raise ValueError(f"Invalid date format: {visit_date}")

            visit = {
                "visit_id": row["visit_id"],
                "visit_date": visit_date,
                "cost": float(row["cost"]) if row["cost"] else None,
            }
            rows.append(json.dumps(visit, separators=(",", ":")))
    return "\n".join(rows)
