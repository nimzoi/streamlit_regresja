# Streamlit - Tłumacz EN → DE

Aplikacja Streamlit tłumacząca tekst z języka angielskiego na język niemiecki,
zbudowana z wykorzystaniem modelu [`Helsinki-NLP/opus-mt-en-de`](https://huggingface.co/Helsinki-NLP/opus-mt-en-de)
z Hugging Face.

Projekt zrealizowany w ramach przedmiotu **SUML** (Środowiska uruchomieniowe AutoML), Lab5: Streamlit.

s25508

## Uruchomienie lokalne

```
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Pierwsze uruchomienie pobierze model z Hugging Face (~300 MB).

## Pliki

- `streamlit_app.py` — interfejs aplikacji
- `translator_utils.py` — ładowanie modelu i funkcja tłumacząca
- `requirements.txt` — zależności
