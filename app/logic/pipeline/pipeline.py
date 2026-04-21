from app.logic.pipeline.parser import parse_input
from app.logic.pipeline.generator import generate_base_prompt
from app.logic.pipeline.enhancer import enhance_prompt
from app.logic.services.image_services import generate_image


def run_pipeline(user_input: str, num_variations=3):
    parsed = parse_input(user_input)

    results = []

    for i in range(num_variations):
        base = generate_base_prompt(parsed)
        final = enhance_prompt(base, parsed)

        image = generate_image(final)

        results.append({
            "variation": i + 1,
            "prompt": final,
            "image": image
        })

    return {
        "parsed": parsed,
        "ads": results
    }