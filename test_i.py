import i as app
import streamlit as st
from transformers import pipeline

def test_predict_positive():
    response = app.post("/predict/",
        json={"text": "Люблю"}
    )
    json_data = response.json() 

    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'