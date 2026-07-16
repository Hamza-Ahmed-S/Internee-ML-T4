# AI-Powered Interview Question Generator

Generates custom technical and behavioral interview questions for interns, tailored to a role/skills/experience profile, using an LLM via the OpenRouter API. New questions are deduplicated against a seed "existing question bank".

Built for the Internee.pk virtual internship task: *AI-Powered Interview Question Generator*.

## Status

Project scaffolding only, so far. The `interview_gen/` package (question bank, prompt builder, API client, response parsing, deduplication, generation orchestrator) and the deliverable notebook are still being built — see `docs/superpowers/plans/2026-07-17-interview-question-generator.md` for the full implementation plan.

## Setup

```bash
pip install -r requirements.txt
```

**API key:** copy `.env.example` to `.env` and fill in your OpenRouter API key:

```
OPENROUTER_API_KEY=<your key>
```

`.env` is gitignored and must never be committed. Get a free key at [openrouter.ai](https://openrouter.ai).

## Planned project structure

```
interview_gen/
  question_bank.py   # seed "existing question bank" data + loader
  prompts.py          # builds the LLM prompt from an intern profile
  client.py            # OpenRouter API call wrapper
  parsing.py           # parses/validates the LLM's JSON response
  dedup.py             # filters out near-duplicate questions
  generator.py         # orchestrates prompt -> API call -> parse -> dedupe
tests/                 # pytest unit tests (API calls are mocked, no real key needed to run tests)
interview_question_generator.ipynb   # main notebook: live demo across sample intern profiles
requirements.txt
.env.example
```

## Notes

Unlike the earlier tasks in this series (T1-T3, which train models from scratch on synthetic data), this task calls a hosted LLM via OpenRouter rather than training anything locally. The test suite mocks the API client, so `pytest` runs without a real network call or API key — only running the actual notebook requires a valid `OPENROUTER_API_KEY`.
