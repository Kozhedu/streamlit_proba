import streamlit as st
from transformers import pipeline

st.header("Определение тональности текстов")
st.subheader("Введите текст для анализа")

text = st.text_area(" ",height=10)

classifier = pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")
st.write ("Тональность текста:")
st.write(classifier(text)[0]["label"])

