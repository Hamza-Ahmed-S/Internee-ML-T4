import pandas as pd

from interview_gen.prompts import build_prompt
from interview_gen.client import call_openrouter
from interview_gen.parsing import parse_questions_response
from interview_gen.dedup import deduplicate_questions


def generate_questions(profile: dict, question_bank: pd.DataFrame) -> pd.DataFrame:
    """Generate interview questions for a profile, deduplicated against
    question_bank. Retries once with a stricter prompt if the model's first
    response isn't valid JSON; raises ValueError if the retry also fails.
    """
    prompt = build_prompt(profile, strict=False)
    raw = call_openrouter(prompt)

    try:
        parsed = parse_questions_response(raw)
    except ValueError:
        strict_prompt = build_prompt(profile, strict=True)
        raw_retry = call_openrouter(strict_prompt)
        parsed = parse_questions_response(raw_retry)

    deduped = deduplicate_questions(parsed, question_bank)
    return pd.DataFrame(deduped, columns=["question", "category", "difficulty"])
