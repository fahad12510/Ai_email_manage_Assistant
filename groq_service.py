import os
from dotenv import load_dotenv
from groq import Groq
from prompts import build_prompt


def generate_message(message_type, tone, rough_message):
    """Send the user's request to Groq and return the generated text."""
    load_dotenv()

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. Add your Groq API key to the .env file."
        )

    # You can change GROQ_MODEL in .env if a model is unavailable.
    model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

    client = Groq(api_key=api_key)
    prompt = build_prompt(message_type, tone, rough_message)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You improve emails and messages while preserving the user's meaning.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
    )

    generated_text = response.choices[0].message.content
    if not generated_text or not generated_text.strip():
        raise RuntimeError("The AI returned an empty response.")

    return generated_text.strip()
