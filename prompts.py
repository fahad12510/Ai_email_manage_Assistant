MESSAGE_TYPES = [
    "Professional Email",
    "Student Message",
    "Leave Application",
    "Formal Request",
]

TONES = {
    "Professional": "Use clear, professional language.",
    "Polite": "Use respectful, courteous, and polite language.",
    "Friendly": "Use warm, natural, and friendly language.",
}


def build_prompt(message_type, tone, rough_message):
    tone_instruction = TONES.get(tone, TONES["Professional"])

    return f"""
You are an AI writing assistant.

Message Type: {message_type}
Tone: {tone}

User's Rough Message:
{rough_message}

Instructions:
- Rewrite the message clearly and naturally.
- Correct grammar, spelling, and punctuation.
- Preserve the user's original meaning.
- Use a suitable format for the selected message type.
- {tone_instruction}
- Do not invent names, dates, reasons, promises, or other facts.
- If important details are missing, use a neutral placeholder only when necessary.
- Return only the final improved message.
""".strip()
