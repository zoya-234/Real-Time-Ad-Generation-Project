from app.logic.llm.gemini_client import call_llm


def parse_input(user_input: str) -> str:
    prompt = f"""
    Extract structured advertisement details.

    Return ONLY valid JSON with:
    product, audience, platform, tone, goal

    If something is missing, infer it.

    Input: {user_input}
    """

    return call_llm(prompt)