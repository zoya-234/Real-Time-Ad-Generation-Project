from app.logic.llm.gemini_client import call_llm
from app.logic.core.style_map import STYLE_MAP
from app.logic.core.platform_rules import PLATFORM_RULES
import json
import random

ANGLE_OPTIONS = [
    "top-down shot",
    "low-angle cinematic shot",
    "close-up macro shot",
    "wide lifestyle shot"
]

LIGHTING_OPTIONS = [
    "golden hour lighting",
    "soft studio lighting",
    "dramatic high contrast lighting",
    "natural daylight"
]


def enhance_prompt(base_prompt: str, parsed_json: str) -> str:
    try:
        data = json.loads(parsed_json)
    except:
        data = {}

    tone = data.get("tone", "").lower()
    platform = data.get("platform", "").lower()

    style_hint = STYLE_MAP.get(tone, "")
    platform_hint = PLATFORM_RULES.get(platform, "")

    angle = random.choice(ANGLE_OPTIONS)
    lighting = random.choice(LIGHTING_OPTIONS)

    prompt = f"""
    Enhance this ad prompt with variation.

    Camera angle: {angle}
    Lighting: {lighting}

    Add cinematic, commercial quality, realism.

    Base Prompt:
    {base_prompt}
    """
    return call_llm(prompt)

