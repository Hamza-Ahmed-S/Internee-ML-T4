import pandas as pd
from interview_gen.dedup import deduplicate_questions


def test_deduplicate_questions_drops_near_duplicate():
    bank = pd.DataFrame({"question": ["What is the difference between a list and a tuple in Python?"]})
    new_questions = [
        {"question": "What is the difference between a list and a tuple in Python?", "category": "technical", "difficulty": "beginner"},
    ]
    result = deduplicate_questions(new_questions, bank)
    assert result == []


def test_deduplicate_questions_keeps_distinct_question():
    bank = pd.DataFrame({"question": ["What is the difference between a list and a tuple in Python?"]})
    new_questions = [
        {"question": "How do you design a scalable microservice architecture?", "category": "technical", "difficulty": "advanced"},
    ]
    result = deduplicate_questions(new_questions, bank)
    assert len(result) == 1
    assert result[0]["question"] == "How do you design a scalable microservice architecture?"


def test_deduplicate_questions_drops_duplicates_within_new_batch_too():
    bank = pd.DataFrame({"question": []})
    new_questions = [
        {"question": "Tell me about a time you led a project.", "category": "behavioral", "difficulty": "intermediate"},
        {"question": "Tell me about a time you led a project.", "category": "behavioral", "difficulty": "intermediate"},
    ]
    result = deduplicate_questions(new_questions, bank)
    assert len(result) == 1


def test_deduplicate_questions_empty_bank_keeps_all():
    bank = pd.DataFrame({"question": []})
    new_questions = [
        {"question": "What is a hash map?", "category": "technical", "difficulty": "beginner"},
        {"question": "Describe your ideal team culture.", "category": "behavioral", "difficulty": "beginner"},
    ]
    result = deduplicate_questions(new_questions, bank)
    assert len(result) == 2
