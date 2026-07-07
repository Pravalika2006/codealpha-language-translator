import streamlit as st
from googletrans import Translator
import pyperclip
from gtts import gTTS
import os

st.set_page_config(page_title="Language Translation Tool", layout="centered")
st.title("🌍 Language Translation Tool")
st.write("Enter text, select languages, and get instant translation")

translator = Translator()

# Dictionary of languages
languages = {
    'English': 'en', 'Hindi': 'hi', 'Telugu': 'te', 'Tamil': 'ta',
    'Kannada': 'kn', 'Marathi': 'mr', 'Bengali': 'bn', 'Gujarati': 'gu',
    'French': 'fr', 'Spanish': 'es', 'German': 'de', 'Chinese': 'zh-cn'
}

# STEP 3: USER INTERFACE
text = st.text_area("Enter text to translate:", height=150, placeholder="Type here...")

col1, col2 = st.columns(2)
with col1:
    src_lang = st.selectbox("Source Language", list(languages.keys()), index=0)
with col2:
    tgt_lang = st.selectbox("Target Language", list(languages.keys()), index=1)

# STEP 4: TRANSLATE LOGIC
if st.button("Translate"):
    if text.strip() != "":
        with st.spinner("Translating..."):
            try:
                result = translator.translate(text, src=languages[src_lang], dest=languages[tgt_lang])
                translated_text = result.text
                
                # STEP 5: DISPLAY RESULT
                st.success("Translated Text:")
                st.text_area("", translated_text, height=150, key="output")
                
                # OPTIONAL 1: COPY BUTTON
                if st.button("📋 Copy Translation"):
                    pyperclip.copy(translated_text)
                    st.info("Copied to clipboard!")
                
                # OPTIONAL 2: TEXT-TO-SPEECH
                tts = gTTS(translated_text, lang=languages[tgt_lang])
                tts.save("translated.mp3")
                st.audio("translated.mp3")
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter some text to translate")