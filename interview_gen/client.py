import os
import requests

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "nvidia/nemotron-nano-9b-v2:free"


def call_openrouter(prompt: str, model: str = DEFAULT_MODEL, timeout: int = 60) -> str:
    """Call the OpenRouter chat completions API with a single user prompt.

    Reads the API key from the OPENROUTER_API_KEY environment variable.
    Raises RuntimeError if the key is missing, and requests.HTTPError if the
    API call itself fails, so failures are visible rather than silently
    swallowed.
    """
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENROUTER_API_KEY is not set. Create a .env file with "
            "OPENROUTER_API_KEY=<your key> (see .env.example)."
        )

    response = requests.post(
        OPENROUTER_URL,
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=timeout,
    )
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]
