def build_prompt(profile: dict, strict: bool = False) -> str:
    """Build the LLM prompt for generating interview questions from a
    structured intern profile.

    profile keys: role (str), tech_skills (list[str]), experience_level (str),
    focus_topics (list[str]).
    """
    skills = ", ".join(profile["tech_skills"])
    topics = ", ".join(profile["focus_topics"])

    prompt = (
        f"You are helping an interviewer prepare for an internship interview.\n\n"
        f"Role: {profile['role']}\n"
        f"Candidate's technical skills: {skills}\n"
        f"Experience level: {profile['experience_level']}\n"
        f"Focus topics: {topics}\n\n"
        f"Generate 6 interview questions tailored to this role and profile: "
        f"a mix of technical and behavioral questions, appropriate for the "
        f"candidate's experience level.\n\n"
        f"Return the questions as a JSON array of objects, where each object "
        f"has exactly these keys: \"question\" (string), \"category\" "
        f"(either \"technical\" or \"behavioral\"), \"difficulty\" (one of "
        f"\"beginner\", \"intermediate\", \"advanced\").\n"
    )

    if strict:
        prompt += (
            "\nIMPORTANT: Return ONLY valid JSON, with no surrounding text, "
            "no markdown code fences, and no explanation before or after the "
            "JSON array."
        )

    return prompt
