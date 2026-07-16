import pytest
from interview_gen.parsing import parse_questions_response


def test_parse_questions_response_valid_json():
    raw = '[{"question": "What is a list?", "category": "technical", "difficulty": "beginner"}]'
    result = parse_questions_response(raw)
    assert result == [{"question": "What is a list?", "category": "technical", "difficulty": "beginner"}]


def test_parse_questions_response_strips_markdown_fences():
    raw = '```json\n[{"question": "Q1", "category": "behavioral", "difficulty": "intermediate"}]\n```'
    result = parse_questions_response(raw)
    assert result == [{"question": "Q1", "category": "behavioral", "difficulty": "intermediate"}]


def test_parse_questions_response_rejects_invalid_json():
    with pytest.raises(ValueError):
        parse_questions_response("this is not json at all")


def test_parse_questions_response_rejects_missing_keys():
    raw = '[{"question": "Q1"}]'
    with pytest.raises(ValueError):
        parse_questions_response(raw)


def test_parse_questions_response_rejects_non_list():
    raw = '{"question": "Q1", "category": "technical", "difficulty": "beginner"}'
    with pytest.raises(ValueError):
        parse_questions_response(raw)
