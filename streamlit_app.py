import streamlit as st

from translator_utils import MODEL_NAME, load_translator, translate

st.set_page_config(page_title="Tłumacz EN-DE", layout="centered")

st.title("Tłumacz angielsko-niemiecki")

st.write(
    "Aplikacja tłumaczy tekst z języka angielskiego na język niemiecki. "
    "Wykorzystuje model Helsinki-NLP/opus-mt-en-de z Hugging Face."
)

st.write(
    "Aby przetłumaczyć tekst, wpisz lub wklej go w pole poniżej "
    "i kliknij przycisk Przetłumacz."
)

mode = st.sidebar.radio("Tryb", ["Tłumacz", "O aplikacji"], index=0)

if mode == "O aplikacji":
    st.subheader("O aplikacji")
    st.write(
        "Projekt zrealizowany w ramach przedmiotu SUML "
        "(Środowiska uruchomieniowe AutoML), Lab5: Streamlit."
    )
    st.write(f"Model: {MODEL_NAME}")
    st.write(
        "Pierwsze uruchomienie może potrwać dłużej, ponieważ model "
        "jest pobierany z Hugging Face. Kolejne tłumaczenia są szybkie."
    )
else:
    with st.spinner("Ładuję model..."):
        try:
            load_translator()
        except Exception as e:
            st.error(f"Nie udało się załadować modelu: {e}")
            st.stop()

    st.subheader("Tekst do tłumaczenia")
    text_in = st.text_area("Tekst po angielsku", height=160)

    if st.button("Przetłumacz"):
        if not text_in.strip():
            st.warning("Podaj tekst do tłumaczenia.")
        else:
            try:
                with st.spinner("Tłumaczę..."):
                    translation = translate(text_in.strip())
                st.success("Gotowe.")
                st.subheader("Tłumaczenie")
                st.text_area("Tekst po niemiecku", value=translation, height=160)
            except Exception as e:
                st.error(f"Błąd podczas tłumaczenia: {e}")

st.write("---")
st.caption("s25508")
