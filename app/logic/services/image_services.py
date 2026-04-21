from __future__ import annotations

import base64
from datetime import datetime
from pathlib import Path
from uuid import uuid4

import google.generativeai as genai

from app.config.settings import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

OUTPUT_DIR = Path("app/logs/generated_images")


def _candidate_image_models() -> list[str]:
    seeds = [
        "gemini-2.0-flash-preview-image-generation",
        "gemini-2.5-flash-image-preview",
        "gemini-3-pro-image-preview",
    ]
    candidates: list[str] = []
    for name in seeds:
        if name not in candidates:
            candidates.append(name)

    return candidates


def _extract_image(response) -> tuple[bytes | None, str | None]:
    candidates = getattr(response, "candidates", None) or []
    for candidate in candidates:
        content = getattr(candidate, "content", None)
        parts = getattr(content, "parts", None) or []
        for part in parts:
            inline_data = getattr(part, "inline_data", None)
            if inline_data is None:
                continue
            mime_type = getattr(inline_data, "mime_type", None)
            data = getattr(inline_data, "data", None)
            if not data or not mime_type or not str(mime_type).startswith("image/"):
                continue
            if isinstance(data, str):
                try:
                    return base64.b64decode(data), str(mime_type)
                except Exception:
                    continue
            if isinstance(data, (bytes, bytearray)):
                return bytes(data), str(mime_type)

    return None, None


def _extension_for_mime(mime_type: str) -> str:
    if "png" in mime_type:
        return "png"
    if "jpeg" in mime_type or "jpg" in mime_type:
        return "jpg"
    if "webp" in mime_type:
        return "webp"
    return "bin"


def generate_image(prompt: str):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    last_error: Exception | None = None

    for model_name in _candidate_image_models():
        try:
            model = genai.GenerativeModel(model_name)
            try:
                response = model.generate_content(
                    prompt,
                    generation_config={"response_modalities": ["TEXT", "IMAGE"]},
                )
            except TypeError:
                response = model.generate_content(prompt)

            image_bytes, mime_type = _extract_image(response)
            if not image_bytes or not mime_type:
                continue

            ext = _extension_for_mime(mime_type)
            filename = f"image_{datetime.now():%Y%m%d_%H%M%S}_{uuid4().hex[:6]}.{ext}"
            output_path = OUTPUT_DIR / filename
            output_path.write_bytes(image_bytes)
            return str(output_path)
        except Exception as e:
            last_error = e

    try:
        if last_error is not None:
            print("Image Generation Error:", last_error)
        return None
    except Exception as e:
        print("Image Generation Error:", e)
        return None