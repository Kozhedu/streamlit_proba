import streamlit as st
from transformers import pipeline

st.header("Анализ тональности текста")
st.subheader("Введите текст для анализа")

text = st.text_area(" ",height=50)

classifier = pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")


st.write(classifier(text))

