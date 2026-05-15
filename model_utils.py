import os
import pickle

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "dane.csv")
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")


def load_data():
    return pd.read_csv(DATA_PATH)


def _fit(df):
    X = df["x"].values.reshape(-1, 1)
    Y = df["y"].values.reshape(-1, 1)
    model = LinearRegression()
    model.fit(X, Y)
    return model


def _save_model(model):
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)


def train_model():
    model = _fit(load_data())
    _save_model(model)
    return model


def load_model():
    if not os.path.exists(MODEL_PATH):
        return train_model()
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)


def get_coefficients(model):
    a = float(model.coef_[0][0])
    b = float(model.intercept_[0])
    return a, b


def predict(x):
    model = load_model()
    X = np.array([[x]], dtype=float)
    return float(model.predict(X)[0][0])


def add_point_and_retrain(x, y):
    df = load_data()
    combined = pd.concat(
        [df, pd.DataFrame({"x": [x], "y": [y]})], ignore_index=True
    )
    model = _fit(combined)
    combined.to_csv(DATA_PATH, index=False)
    _save_model(model)
    return model
