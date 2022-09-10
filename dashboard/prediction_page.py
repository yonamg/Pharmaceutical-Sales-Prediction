import pickle
import dvc.api
import pandas as pd
import streamlit as st
from PIL import Image



model_path = 'model/2022-09-08-21-17-38.pkl'
repo = 'https://github.com/yonamg/Pharmaceutical-Sales-Prediction'
model_ver = '9d7caa4'
model_url = dvc.api.get_url(
    path=model_path,
    repo=repo,
    rev=model_ver
)


def load_model():
    pickle_in = open(model_url, 'rb')
    random_fore_model = pickle.load(pickle_in)
    return random_fore_model


def prdict_app():
    st.title("Prdict Sales")

    sales_score = st.slider("Sales", min_value=0.0,
                          max_value=2.0, step=0.1)
    salesD_score = st.slider("Sales Assortment", min_value=0.0,
                          max_value=2.0, step=0.1)

    if st.button("Predict"):
        model = load_model()
        result = model.predict([[sales_score, salesD_score]])

        st.success(f"The sales prediction is {result[0][0]}")