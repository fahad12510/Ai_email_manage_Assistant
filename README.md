# AI Email & Message Assistant

A beginner-friendly Python terminal application that improves rough messages using the Groq API.

## Features

- Generate Professional Emails, Student Messages, Leave Applications, and Formal Requests.
- Choose Professional, Polite, or Friendly tone.
- Correct grammar and improve clarity while preserving the original meaning.
- Regenerate a message using a new Groq API request.
- Validate empty input and handle missing API keys or API errors.
- Keep the API key in a local `.env` file.

## Project files

```text
AI_Email_Message_Assistant/
├── main.py
├── groq_service.py
├── prompts.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
└── README.md
```

## Requirements

- Python 3.10 or newer
- Internet connection
- A Groq API key

## Installation on Windows

1. Open this folder in VS Code or File Explorer.
2. Open a terminal inside the project folder.
3. (Optional but recommended) Create a virtual environment:

   ```bash
   py -m venv .venv
   .venv\\Scripts\\activate
   ```

4. Install the required packages:

   ```bash
   py -m pip install -r requirements.txt
   ```

5. Open the `.env` file and add your own API key:

   ```env
   GROQ_API_KEY=your_actual_api_key_here
   GROQ_MODEL=llama-3.3-70b-versatile
   ```

6. Save the file and run the program:

   ```bash
   py main.py
   ```

## Getting a Groq API key

Create or sign in to your Groq account at https://console.groq.com/ and create an API key in the API Keys section. Keep it private.

The model name is configurable through `GROQ_MODEL`. If the model is unavailable in your account, use a currently supported chat model listed in the Groq documentation:
https://console.groq.com/docs/models

## GitHub security

- The `.env` file is excluded by `.gitignore`.
- Never publish your real API key.
- Upload `.env.example` so other users know which environment variables are required.

## How it works

1. `main.py` displays menus and collects the category, tone, and rough message.
2. `prompts.py` builds a prompt using the selected options and rough text.
3. `groq_service.py` sends the prompt to Groq and returns the generated text.
4. `main.py` displays the response and lets the user regenerate or start another message.

## Test ideas

- Ask for a professional email about an assignment deadline.
- Enter a short leave request.
- Ask for a friendly message requesting class notes.
- Submit an empty message and confirm that the program asks again.
- Temporarily leave the API key blank and confirm that a clear configuration error appears.

## Note

The application requires a working Groq API key and internet connection to generate real AI responses. It does not use hardcoded sample responses.

## Web version (Flask)

Run `py -m pip install -r requirements.txt`, add your Groq key to `.env`, run `py app.py`, then open `http://127.0.0.1:5000` in your browser. The terminal version still runs with `py main.py`.
