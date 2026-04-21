ad-gen-agent/
│
├── app/                        # Core application logic
│   ├── __init__.py
│   │
│   ├── llm/                   # LLM interaction layer
│   │   ├── __init__.py
│   │   ├── gemini_client.py   # Gemini API wrapper
│   │
│   ├── pipeline/              # Prompt pipeline (your main logic)
│   │   ├── __init__.py
│   │   ├── parser.py          # Step 1: Input → JSON
│   │   ├── generator.py       # Step 2: Base prompt
│   │   ├── enhancer.py        # Step 3: Enhanced prompt
│   │   ├── pipeline.py        # Full pipeline orchestration
│   │
│   ├── core/                  # Business logic rules
│   │   ├── __init__.py
│   │   ├── style_map.py       # Tone → style mapping
│   │   ├── platform_rules.py  # Platform optimization rules
│   │
│   ├── models/                # Data schemas (optional but good practice)
│   │   ├── __init__.py
│   │   ├── ad_input.py        # Input schema
│   │   ├── prompt_output.py   # Output schema
│   │
│   ├── services/              # External integrations
│   │   ├── __init__.py
│   │   ├── image_service.py   # Gemini image generation
│   │
│   └── utils/                 # Helper functions
│       ├── __init__.py
│       ├── json_utils.py      # JSON cleaning/parsing
│       ├── logger.py          # Logging setup
│
├── config/                    # Config files
│   ├── settings.py            # API keys, model configs
│
├── tests/                     # Unit tests
│   ├── test_pipeline.py
│
├── logs/                      # Logs (auto-generated)
│   └── app.log
│
├── .env                       # API keys (DO NOT COMMIT)
├── requirements.txt
├── README.md
├── main.py                    # CLI entry point
└── streamlit_app.py           # Optional UI