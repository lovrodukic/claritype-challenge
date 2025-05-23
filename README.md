# Claritype Intern Take‑home – CSV → JSON Converter

## Context
`src/convert.py` converts a CSV file of dental visits into JSON Lines (one
JSON object per line). The current implementation passes a smoke test but
**fails** on real‑world edge cases.

## Your Task
1. Run **`pytest`** – three tests fail.
2. Fix `src/convert.py` so **all tests pass** without breaking the public
   function signature (`csv_to_json_lines(path) -> str`).
3. Keep your patch concise (≈ ≤30 added lines).
4. Add **≤150 words** explaining:
   * Root cause(s)
   * Your fix
   * Further hardening you’d do in production.

You may search the web or use ChatGPT, but the explanation must be yours.

## Setup (Python ≥3.8)
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest          # should show 3 failures initially
```

## Data contract
* **visit_id** – unique string (raise `ValueError` on duplicates)
* **visit_date** – ISO 8601 `YYYY-MM-DD` (raise on invalid formats)
* **cost** – number or `null` if empty

## Submission
* Patch / GitHub link
* 150‑word explanation
* (Optional) ≤3‑min Loom or MP4 walkthrough
