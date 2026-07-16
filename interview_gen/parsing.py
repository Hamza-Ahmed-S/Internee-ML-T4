import json
import re

REQUIRED_KEYS = {"question", "category", "difficulty"}


def parse_questions_response(raw_text: str) -> list[dict]:
    """Parse an LLM's raw text response into a validated list of question dicts.

    Strips markdown code fences if present, then requires the result to be a
    JSON array of objects each containing REQUIRED_KEYS. Raises ValueError on
    any malformed input so callers can decide whether to retry.
    """
    cleaned = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw_text.strip())

    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Response is not valid JSON: {exc}") from exc

    if not isinstance(data, list):
        raise ValueError("Expected a JSON array of question objects.")

    for item in data:
        if not isinstance(item, dict) or not REQUIRED_KEYS <= set(item.keys()):
            raise ValueError(
                f"Each question object must contain keys {REQUIRED_KEYS}, got: {item}"
            )

    return data
