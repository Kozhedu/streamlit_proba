import streamlit as st
import pandas as pd
from transformers import pipeline


page = st.sidebar.selectbox('Выберите страницу:',('Загрузка файла','Определение тональности', "Графики"))

if page == 'Загрузка файла':

    uploaded_file = st.file_uploader("Загрузите csv файл")
    if uploaded_file is not None:
    # сохраняем в датафрейм и читаем:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)


elif page == 'Определение тональности':
    model=pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")
    df_model = dataframe.copy()
    result = st.button("Определить тональность сообщений")
    lst = []
    for i in df_model["text"]:
        lst.append(model(str(i))[0]["label"])
    df_model["Sentinent"]=pd.DataFrame(lst)
    st.write(df_model)


elif page == 'Графики':
    size = st.text_input('Matrix ')