import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

from model_utils import (
    add_point_and_retrain,
    get_coefficients,
    load_data,
    load_model,
    predict,
)

st.set_page_config(page_title="Regresja liniowa", layout="centered")

st.title("Regresja liniowa")

st.write(
    "Aplikacja pokazuje działanie modelu regresji liniowej. "
    "Możesz przewidzieć wartość y dla podanego x, dopisać nowy punkt "
    "i przetrenować model od nowa."
)

df = load_data()
model = load_model()
a, b = get_coefficients(model)

st.subheader("Dane")
st.dataframe(df, use_container_width=True)
st.write(f"Model: y = {a:.4f} · x + {b:.4f}")

st.subheader("Przewidywanie")
x_input = st.number_input("Podaj x", value=2.5, step=0.5, format="%.2f")
if st.button("Przewiduj"):
    try:
        with st.spinner("Liczę..."):
            y_pred = predict(float(x_input))
        st.success(f"y = {y_pred:.4f}")
    except Exception as e:
        st.error(f"Błąd: {e}")

st.subheader("Dodaj punkt i przetrenuj")
with st.form("add_form"):
    new_x = st.number_input("Nowy x", value=11.0, step=1.0, format="%.2f")
    new_y = st.number_input("Nowy y", value=21.5, step=1.0, format="%.2f")
    submit = st.form_submit_button("Zapisz i przetrenuj")

if submit:
    try:
        with st.spinner("Trenuję model..."):
            model = add_point_and_retrain(float(new_x), float(new_y))
            a, b = get_coefficients(model)
            df = load_data()
        st.success(f"Gotowe. Nowe a = {a:.4f}, b = {b:.4f}")
    except Exception as e:
        st.error(f"Błąd: {e}")

st.subheader("Wykres")
fig, ax = plt.subplots()
ax.scatter(df["x"], df["y"], label="Dane")
x_line = np.linspace(df["x"].min() - 1, df["x"].max() + 1, 100)
ax.plot(x_line, a * x_line + b, color="red", label="Regresja")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid(alpha=0.3)
st.pyplot(fig)

st.write("---")
st.caption("s25508")
