# CodeAlpha Language Translation Tool

A simple language translation web app built with **Python** and **Streamlit**, using Google Translate (via `deep-translator`) for English ↔ Tamil and other languages.

## Features

- Select source and target languages
- Translate text between English, Tamil, Hindi, Spanish, French, and more
- Display translated result in the UI
- Copy translated text to clipboard (copy icon on the result box)

## Project structure

```
CodeAlpha_LanguageTranslationTool/
├── app.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.8+
- Internet connection (for the translation service)

## Setup

1. Open a terminal in this folder.

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app.py
```

4. Open the URL shown in the terminal (usually `http://localhost:8501`).

## Usage

1. Choose the **source** and **target** languages.
2. Type or paste text in the input box.
3. Click **Translate**.
4. Click the copy icon on the result to copy the translation.

## Tech stack

| Tool | Role |
|------|------|
| Python | Core language |
| Streamlit | User interface |
| deep-translator (Google Translate) | Translation service |

## CodeAlpha internship

This project meets the Language Translation Tool task requirements: UI, language selection, send text for translation, and display the result.
