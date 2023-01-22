import streamlit as st
import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import numpy as np

#загружаю модель
@st.cache
def read_data(uploaded_file):
    return pd.read_csv(uploaded_file)

datafile = st.sidebar.file_uploader("Загрузите файл csv", ["csv"])
if datafile is None:
    st.info("""Загрузите набор данных (.csv) на боковой панели, чтобы приступить к работе.""")
    st.stop()

data = read_data(datafile).copy()

#обучение модели
model=pipeline("sentiment-analysis",   
                      "blanchefort/rubert-base-cased-sentiment")
                      
result = st.sidebar.button('Распознать')

df_model = data.copy()

if result:
    lst = []
    for i in df_model["text"]:
        lst.append(model(str(i))[0]["label"])
        df_model["Sentinent"]=pd.DataFrame(lst)



#Первый график

fig = plt.figure()
palette = sns.color_palette('PiYG_r', 15)
plt.title('Распределение настроений')
sns.countplot(df_model['Sentinent'], palette=palette)
st.pyplot(fig)

#Второй график

comment_words = ''

for val in df_model.text:
    val = str(val)
    tokens = val.split()
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
     
    comment_words += " ".join(tokens)+" "

wordcloud = WordCloud(background_color = "white").generate(comment_words)

fig = plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot(fig)

#Эксперимент




