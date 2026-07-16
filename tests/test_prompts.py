from interview_gen.prompts import build_prompt

SAMPLE_PROFILE = {
    "role": "Data Analyst Intern",
    "tech_skills": ["Python", "SQL"],
    "experience_level": "beginner",
    "focus_topics": ["data cleaning", "visualization"],
}


def test_build_prompt_includes_all_profile_fields():
    prompt = build_prompt(SAMPLE_PROFILE)
    assert "Data Analyst Intern" in prompt
    assert "Python" in prompt
    assert "SQL" in prompt
    assert "beginner" in prompt
    assert "data cleaning" in prompt
    assert "visualization" in prompt


def test_build_prompt_requests_json_output():
    prompt = build_prompt(SAMPLE_PROFILE)
    assert "JSON" in prompt
    assert "question" in prompt
    assert "category" in prompt
    assert "difficulty" in prompt


def test_build_prompt_strict_mode_adds_stricter_instruction():
    normal = build_prompt(SAMPLE_PROFILE, strict=False)
    strict = build_prompt(SAMPLE_PROFILE, strict=True)
    assert len(strict) > len(normal)
    assert "ONLY valid JSON" in strict
