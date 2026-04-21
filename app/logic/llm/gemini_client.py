import google.generativeai as genai
from app.config.settings import GEMINI_API_KEY, MODEL_NAME

genai.configure(api_key=GEMINI_API_KEY)


def _candidate_models() -> list[str]:
    # Try the configured model first, then a small static fallback list.
    seeds = [
        MODEL_NAME,
        "gemini-1.5-flash-latest",
        "gemini-1.5-pro-latest",
        "gemini-pro"
    ]
    candidates: list[str] = []
    for name in seeds:
        if name and name not in candidates:
            candidates.append(name)

    return candidates


def call_llm(prompt: str) -> str:
    last_error: Exception | None = None
    for model_name in _candidate_models():
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            text = getattr(response, "text", "")
            if text:
                return text.strip()
        except Exception as e:
            last_error = e

    if last_error is not None:
        print("LLM Error:", last_error)
    return ""