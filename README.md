# AI Email & Message Assistant

A beginner-friendly Python terminal application that improves rough emails, student messages, leave applications, and formal requests using the Groq API.

## Features

- Main menu with a continuous `while` loop
- Four message categories
- Three writing tones: Professional, Polite, and Friendly
- Empty-input validation
- Dynamic prompt construction
- Real Groq API request (not hardcoded responses)
- Regenerate option sends a fresh API request
- Basic configuration and API error handling

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

- Python 3.9 or newer
- Internet connection
- A Groq API key

## Setup on Windows

1. Open this folder in VS Code or a terminal.
2. Create a virtual environment (recommended):

   ```powershell
   py -m venv .venv
   ```

3. Activate it:

   ```powershell
   .venv\\Scripts\\activate
   ```

4. Install dependencies:

   ```powershell
   py -m pip install -r requirements.txt
   ```

5. Create an account at https://console.groq.com/ and generate an API key.
6. Create a file named `.env` in this folder. Add your key:

   ```env
   GROQ_API_KEY=your_actual_api_key_here
   GROQ_MODEL=llama-3.3-70b-versatile
   ```

   The model shown is a default example. If it is unavailable in your Groq account, replace it with a currently supported model.

7. Run the program:

   ```powershell
   py main.py
   ```

## Important security note

Never share your API key or upload `.env` to GitHub. The `.gitignore` file excludes it. Upload `.env.example` instead.

## GitHub upload

From inside the project folder:

```powershell
git init
git add .
git commit -m "Add AI Email and Message Assistant"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/AI_Email_Message_Assistant.git
git push -u origin main
```

Replace the URL with your own GitHub repository URL.

## How it works

1. The user selects a message category and tone.
2. The program asks for rough text and checks that it is not empty.
3. `prompts.py` builds a prompt using the selected options.
4. `groq_service.py` sends the prompt to Groq.
5. `main.py` displays the generated message.
6. Regenerate sends another API request.

## Testing checklist

- Try all four message categories.
- Try all three tones.
- Press Enter without typing a message and confirm it asks again.
- Test the regenerate option.
- Temporarily remove the API key from `.env` and confirm a clear configuration error appears.
