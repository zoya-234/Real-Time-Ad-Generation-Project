from app.logic.pipeline.pipeline import run_pipeline


if __name__ == "__main__":
    user_input = input("Enter your ad idea: ")

    result = run_pipeline(user_input)

    print("\n--- Parsed JSON ---")
    print(result["parsed"])

    for ad in result["ads"]:
        print(f"\n--- Variation {ad['variation']} Prompt ---")
        print(ad["prompt"])

        print(f"\n--- Variation {ad['variation']} Image Output ---")
        print(ad["image"])
