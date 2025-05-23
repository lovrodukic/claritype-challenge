# Claritype Intern Take‑home – CSV → JSON Converter

## Patch Explanation

### What was Wrong

- The original function did not strictly enforce ISO-8601 format (`YYYY-MM-DD`).
- Duplicate `visit_id` entries were allowed without raising an exception.
- Empty cost fields should have been treated as `None` but were incorrectly `0.0`.

### Fixes

- I used regular expression matching to ensure that the pattern of the input date
  complies with ISO-8601. I knew about regex but was unfamiliar with formatting
  using `re` in Python, so I searched how they work on Google.
- I used a set to track all seen `visit_id` entries. For each row in the CSV,
  if it was already seen, raise an exception.
- When adding `"cost"` to the JSON, instead of adding `0.0` if that value was not
  provided, I changed it to `None`.

### Follow-up Improvements

- I think ISO-8601 has more options such as timestamp. I added some optional
  parameters in the regex that would handle such cases, but did not test them. In
  the future, I would add more test cases to make sure my function is fully
  compliant to ISO-8601.
- Improve error handling. So far I just raise ValueError with a message. Ideally,
  I would define custom error classes and could provide more details in the error
  message such as CSV row number.
