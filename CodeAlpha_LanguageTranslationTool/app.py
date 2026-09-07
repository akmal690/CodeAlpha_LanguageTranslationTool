"""
CodeAlpha Language Translation Tool
Streamlit UI for translating text between English, Tamil, and other languages.
"""

import streamlit as st
from deep_translator import GoogleTranslator

# Language display name → Google Translate language code
LANGUAGES = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Portuguese": "pt",
    "Russian": "ru",
    "Italian": "it",
    "Bengali": "bn",
    "Telugu": "te",
    "Malayalam": "ml",
    "Kannada": "kn",
    "Urdu": "ur",
}

LANG_NAMES = list(LANGUAGES.keys())

st.set_page_config(
    page_title="CodeAlpha Language Translation Tool",
    page_icon="🌐",
    layout="centered",
)

st.title("🌐 Language Translation Tool")
st.caption("CodeAlpha Internship Project — Translate text between English, Tamil, and more.")

if "source_lang" not in st.session_state:
    st.session_state.source_lang = "English"
if "target_lang" not in st.session_state:
    st.session_state.target_lang = "Tamil"

def swap_languages():
    st.session_state.source_lang, st.session_state.target_lang = (
        st.session_state.target_lang,
        st.session_state.source_lang,
    )

col1, col2 = st.columns(2)
with col1:
    st.selectbox("Source language", LANG_NAMES, key="source_lang")
with col2:
    st.selectbox("Target language", LANG_NAMES, key="target_lang")

st.button("⇄ Swap languages", on_click=swap_languages, use_container_width=True)

text = st.text_area(
    "Enter text to translate",
    height=150,
    placeholder="Type or paste your text here…",
)

if st.button("Translate", type="primary", use_container_width=True):
    source_lang = st.session_state.source_lang
    target_lang = st.session_state.target_lang

    if not text.strip():
        st.warning("Please enter some text to translate.")
    elif source_lang == target_lang:
        st.info("Source and target languages are the same. Showing original text.")
        st.subheader("Result")
        st.code(text, language=None)
        st.session_state["last_translation"] = text
    else:
        try:
            with st.spinner("Translating…"):
                result = GoogleTranslator(
                    source=LANGUAGES[source_lang],
                    target=LANGUAGES[target_lang],
                ).translate(text)
            st.session_state["last_translation"] = result
            st.session_state["last_pair"] = (source_lang, target_lang)
        except Exception as exc:
            st.error(f"Translation failed: {exc}")

if "last_translation" in st.session_state:
    pair = st.session_state.get("last_pair")
    st.subheader("Translated text")
    st.code(st.session_state["last_translation"], language=None)
    if pair:
        st.success(f"Translated from **{pair[0]}** → **{pair[1]}**")
    st.caption("Click the copy icon in the top-right of the result box to copy.")

st.divider()
st.markdown(
    """
**How to use**
1. Choose source and target languages (e.g. English ↔ Tamil).
2. Enter the text you want to translate.
3. Click **Translate**.
4. Use the copy icon on the result to copy the translated text.
"""
)
