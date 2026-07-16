from unittest.mock import patch
import pandas as pd
from interview_gen.generator import generate_questions

SAMPLE_PROFILE = {
    "role": "Data Analyst Intern",
    "tech_skills": ["Python", "SQL"],
    "experience_level": "beginner",
    "focus_topics": ["data cleaning", "visualization"],
}

VALID_RESPONSE = (
    '[{"question": "How would you clean a messy dataset?", "category": "technical", "difficulty": "beginner"},'
    '{"question": "Tell me about a time you handled ambiguous requirements.", "category": "behavioral", "difficulty": "beginner"}]'
)


@patch("interview_gen.generator.call_openrouter")
def test_generate_questions_returns_dataframe(mock_call):
    mock_call.return_value = VALID_RESPONSE
    bank = pd.DataFrame({"question": ["Some unrelated existing question."]})

    result = generate_questions(SAMPLE_PROFILE, bank)

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2
    assert "question" in result.columns
    mock_call.assert_called_once()


@patch("interview_gen.generator.call_openrouter")
def test_generate_questions_filters_duplicates_against_bank(mock_call):
    mock_call.return_value = VALID_RESPONSE
    bank = pd.DataFrame({"question": ["How would you clean a messy dataset?"]})

    result = generate_questions(SAMPLE_PROFILE, bank)

    assert len(result) == 1
    assert result.iloc[0]["question"] == "Tell me about a time you handled ambiguous requirements."


@patch("interview_gen.generator.call_openrouter")
def test_generate_questions_retries_once_on_malformed_json_then_succeeds(mock_call):
    mock_call.side_effect = ["not json", VALID_RESPONSE]
    bank = pd.DataFrame({"question": []})

    result = generate_questions(SAMPLE_PROFILE, bank)

    assert len(result) == 2
    assert mock_call.call_count == 2


@patch("interview_gen.generator.call_openrouter")
def test_generate_questions_raises_after_retry_also_fails(mock_call):
    mock_call.side_effect = ["not json", "still not json"]
    bank = pd.DataFrame({"question": []})

    try:
        generate_questions(SAMPLE_PROFILE, bank)
        assert False, "expected ValueError"
    except ValueError:
        pass
    assert mock_call.call_count == 2
