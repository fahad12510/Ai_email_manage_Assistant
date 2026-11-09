import os
from dotenv import load_dotenv
from groq import Groq
from prompts import build_prompt

load_dotenv()


def generate_message(message_type, tone, rough_message):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. Add your API key to the .env file."
        )

    model_name = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
    client = Groq(api_key=api_key)

    prompt = build_prompt(message_type, tone, rough_message)

    completion = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": "You improve messages while preserving the user's meaning."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_completion_tokens=700
    )

    response = completion.choices[0].message.content

    if not response:
        raise ValueError("The AI returned an empty response. Please try again.")

    return response.strip()
