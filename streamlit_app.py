import streamlit as st

from translator_utils import MODEL_NAME, load_translator, translate

st.set_page_config(
    page_title="EN → DE Translator",
    page_icon="🇩🇪",
    layout="centered",
)

st.title("🇬🇧 → 🇩🇪 Tłumacz angielsko-niemiecki")

st.markdown(
    """
    Aplikacja tłumaczy tekst z **języka angielskiego** na **język niemiecki**.

    Pod maską działa model [`Helsinki-NLP/opus-mt-en-de`](https://huggingface.co/Helsinki-NLP/opus-mt-en-de)
    pobrany z Hugging Face.

    **Jak korzystać:**
    1. Wpisz lub wklej tekst po angielsku w pole poniżej.
    2. Kliknij **Przetłumacz**.
    3. Tłumaczenie pojawi się w polu wynikowym — możesz je skopiować.
    """
)

mode = st.sidebar.radio(
    "Tryb",
    ["Tłumacz", "O aplikacji"],
    index=0,
)

if mode == "O aplikacji":
    st.subheader("O aplikacji")
    st.write(
        "Projekt zrealizowany w ramach przedmiotu SUML "
        "(Środowiska uruchomieniowe AutoML), Lab5: Streamlit."
    )
    st.write(f"Model: `{MODEL_NAME}`")
    st.write(
        "Pierwsze uruchomienie może potrwać dłużej — model jest "
        "pobierany z Hugging Face i ładowany do pamięci. Kolejne "
        "tłumaczenia są już szybkie (model jest cache'owany)."
    )
else:
    with st.status("Ładuję model tłumaczący...", expanded=False) as status:
        try:
            load_translator()
            status.update(label="Model gotowy ✅", state="complete")
        except Exception as e:
            status.update(label="Nie udało się załadować modelu", state="error")
            st.error(f"Błąd ładowania modelu: {e}")
            st.stop()

    st.subheader("Tekst do tłumaczenia")
    text_in = st.text_area(
        "Tekst po angielsku",
        height=160,
        placeholder="Type or paste English text here...",
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        go = st.button("Przetłumacz", type="primary", use_container_width=True)
    with col2:
        clear = st.button("Wyczyść", use_container_width=True)

    if clear:
        st.rerun()

    if go:
        if not text_in.strip():
            st.warning("Podaj tekst do tłumaczenia.")
        else:
            try:
                with st.spinner("Tłumaczę..."):
                    translation = translate(text_in.strip())
                st.success("Gotowe!")
                st.subheader("Tłumaczenie (DE)")
                st.text_area(
                    "Tekst po niemiecku",
                    value=translation,
                    height=160,
                )
            except Exception as e:
                st.error(f"Wystąpił błąd podczas tłumaczenia: {e}")

st.write("---")
st.caption("s25508")
