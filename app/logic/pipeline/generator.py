from app.logic.llm.gemini_client import call_llm


def generate_base_prompt(parsed_json: str) -> str:
    prompt = f"""
    Convert the following JSON into a structured image generation prompt.

    Rules:
    - Include product, audience, platform
    - Add scene, lighting, composition

    JSON:
    {parsed_json}
    """

    return call_llm(prompt)