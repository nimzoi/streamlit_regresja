import streamlit as st
from transformers import pipeline

MODEL_NAME = "Helsinki-NLP/opus-mt-en-de"


@st.cache_resource(show_spinner=False)
def load_translator():
    return pipeline("translation", model=MODEL_NAME)


def translate(text: str) -> str:
    translator = load_translator()
    result = translator(text, max_length=512)
    return result[0]["translation_text"]
