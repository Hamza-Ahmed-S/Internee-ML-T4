from difflib import SequenceMatcher
import pandas as pd

SIMILARITY_THRESHOLD = 0.8


def _is_similar(a: str, b: str) -> bool:
    return SequenceMatcher(None, a.lower(), b.lower()).ratio() >= SIMILARITY_THRESHOLD


def deduplicate_questions(new_questions: list[dict], existing_bank: pd.DataFrame) -> list[dict]:
    """Filter out questions from new_questions that are near-duplicates of
    anything already in existing_bank['question'], or of each other within
    the new batch itself.
    """
    known_texts = list(existing_bank["question"])
    kept: list[dict] = []

    for item in new_questions:
        text = item["question"]
        if any(_is_similar(text, known) for known in known_texts):
            continue
        kept.append(item)
        known_texts.append(text)

    return kept
