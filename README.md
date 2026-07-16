# AI-Powered Interview Question Generator

Generates custom technical and behavioral interview questions for interns, tailored to a role/skills/experience profile, using an LLM via the OpenRouter API. New questions are deduplicated against a seed "existing question bank".

Built for the Internee.pk virtual internship task: *AI-Powered Interview Question Generator*.

## Overview

- Seeds an "existing question bank" of ~18 hand-written technical/behavioral questions (per the brief's "existing question banks" data input)
- Builds a prompt from a structured intern profile (role, tech skills, experience level, focus topics) and calls an LLM via the **OpenRouter** API
- Parses the model's JSON response, with one automatic retry using a stricter prompt if the first response isn't valid JSON
- Deduplicates newly generated questions against the existing bank (and against each other) using text-similarity matching, so repeated runs don't resurface the same questions
- Demonstrates generation across 3 sample intern profiles (Data Analyst, Backend Engineering, Machine Learning interns), with the bank growing across profiles in the same run

## Project structure

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

## Setup

```bash
pip install -r requirements.txt
```

**API key:** copy `.env.example` to `.env` and fill in your OpenRouter API key:

```
OPENROUTER_API_KEY=<your key>
```

`.env` is gitignored and must never be committed. Get a free key at [openrouter.ai](https://openrouter.ai).

## Run

Open and run the notebook (requires a valid `OPENROUTER_API_KEY` in `.env`, since it makes live API calls):

```bash
jupyter notebook interview_question_generator.ipynb
```

Or run the test suite (no API key or network access required — the API client is mocked):

```bash
pytest -v
```

## Notes

Unlike the earlier tasks in this series (T1-T3, which train models from scratch on synthetic data), this task calls a hosted LLM via OpenRouter rather than training anything locally. The test suite mocks the API client, so `pytest` runs without a real network call or API key — only running the actual notebook requires a valid `OPENROUTER_API_KEY`.

The default model (`interview_gen/client.py`'s `DEFAULT_MODEL`) is set to a free-tier OpenRouter model. Free-tier models can be temporarily rate-limited or occasionally removed/renamed upstream — if you get a 404 or persistent 429, check `https://openrouter.ai/api/v1/models` (filter for IDs ending in `:free`) for a currently available alternative and update `DEFAULT_MODEL`.

The generation pipeline was verified end-to-end with real API calls before the notebook was finalized: `meta-llama/llama-3.1-8b-instruct:free` (originally chosen) had been removed from the free tier, and the next choice (`meta-llama/llama-3.3-70b-instruct:free`) was temporarily upstream-rate-limited; `nvidia/nemotron-nano-9b-v2:free` worked reliably and was set as the default.
