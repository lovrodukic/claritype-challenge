import tempfile, os, json, pytest
from src.convert import csv_to_json_lines

CSV_HEADER = "visit_id,visit_date,cost\n"

def _write_tmp(csv_body: str):
    fp = tempfile.NamedTemporaryFile("w+", delete=False, suffix=".csv")
    fp.write(CSV_HEADER + csv_body)
    fp.flush()
    fp.close()
    return fp.name

def test_invalid_date_format():
    # date in MM/DD/YY format should raise ValueError
    csv_body = "v1,03/14/25,123.45\n"
    path = _write_tmp(csv_body)
    with pytest.raises(ValueError):
        csv_to_json_lines(path)
    os.unlink(path)

def test_null_cost_field():
    csv_body = "v2,2025-03-14,\n"
    path = _write_tmp(csv_body)
    out = csv_to_json_lines(path)
    os.unlink(path)
    obj = json.loads(out)
    assert obj["cost"] is None, "Empty cost field should map to null"

def test_duplicate_visit_id():
    csv_body = "v3,2025-03-14,10\n"                    "v3,2025-03-15,20\n"
    path = _write_tmp(csv_body)
    with pytest.raises(ValueError):
        csv_to_json_lines(path)
    os.unlink(path)
