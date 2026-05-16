# Streamlit - tłumacz EN -> DE

Aplikacja Streamlit tłumacząca tekst z angielskiego na niemiecki
(SUML, Lab5). Model Helsinki-NLP/opus-mt-en-de z Hugging Face.

s25508

## Uruchomienie

```
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Pierwsze uruchomienie pobiera model z Hugging Face (ok. 300 MB).

## Pliki

- `streamlit_app.py` - aplikacja
- `translator_utils.py` - ładowanie modelu i funkcja tłumacząca
- `requirements.txt` - zależności
