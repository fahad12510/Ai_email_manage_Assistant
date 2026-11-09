MESSAGE_TYPES = {
    1: "Professional Email",
    2: "Student Message",
    3: "Leave Application",
    4: "Formal Request"
}

TONES = {
    1: "Professional",
    2: "Polite",
    3: "Friendly"
}


def build_prompt(message_type, tone, rough_message):
    prompt = f"""
You are an AI writing assistant.

Message Type: {message_type}
Tone: {tone}

User's Rough Message:
{rough_message}

Instructions:
- Rewrite the message clearly and naturally.
- Correct grammar, spelling, and punctuation.
- Maintain the original meaning.
- Use the selected tone and suitable format.
- Do not invent names, dates, reasons, or other facts.
- Do not add details that the user did not provide.
- Return only the final improved message.
"""
    return prompt.strip()
