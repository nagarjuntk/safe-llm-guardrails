import time
from google import genai
from google.genai import types
from config import SYSTEM_PROMPT

client = genai.Client()  # reads GEMINI_API_KEY automatically

MODELS = [
    "gemini-3.5-flash",
    "gemini-3-flash-preview",
    "gemma-3-27b-it",
]

def get_llm_response(user_input):
    last_error = None
    for model in MODELS:
        for attempt in range(2):  # try each model twice
            try:
                if model.startswith("gemma"):
                    # Gemma may not accept system instructions, so put it in the prompt
                    response = client.models.generate_content(
                        model=model,
                        contents=SYSTEM_PROMPT + "\n\nUser: " + user_input,
                    )
                else:
                    response = client.models.generate_content(
                        model=model,
                        contents=user_input,
                        config=types.GenerateContentConfig(
                            system_instruction=SYSTEM_PROMPT,
                            max_output_tokens=500,
                        ),
                    )
                return response.text
            except Exception as e:
                last_error = e
                time.sleep(2)
    raise last_error  