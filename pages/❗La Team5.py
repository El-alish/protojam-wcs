import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go  # for 3D plot visualization
import plotly.figure_factory as ff
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)

from wordcloud import WordCloud
from langdetect import detect
from datetime import datetime
import plotly.figure_factory as ff
st.set_page_config(layout="wide")
st.header('La Team 5', divider='rainbow')
with st.sidebar:
    #st.image('https://media4.giphy.com/media/PqcBU8T4SeuO3kOMVu/giphy.gif?cid=ecf05e47ayiowxuub1416x1q3ttwa8hrcpfhbje9g2ivq1m1&ep=v1_gifs_related&rid=giphy.gif&ct=g')
    st.image('https://cdn.discordapp.com/attachments/1210594061346672687/1240680856251531425/Designer_2.jpeg?ex=66477196&is=66462016&hm=e3ca395793ea5a222f3e435c5ad402ad2da2ac848b448384a441ccfe357b5947&')
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.write('Alain Recuze')
    st.image('https://cdn.discordapp.com/attachments/1210594061346672687/1240681461397585990/Designer_3.jpeg?ex=66477227&is=664620a7&hm=56ad4966549361118237b6d8b8a5fab4bd01b2f479b5a2da247b2be0f22d0b60&')

with col2:
    st.write('Florian Soumilliard')
    st.image('https://neural.love/cdn/thumbnails/1edc9faa-ff7e-60b4-9345-db4d71a456af/72815e39-10a4-5398-bf22-2e9fd6f9acfc.webp?Expires=1719791999&Signature=0~ZXqneNiXHweY8Bh8B9tGy~z44nuLX~xHZzg7JTnBMq3ci1L8ne4a5U7D2RmnpaCpoZl0gW54v3xROskq041z4TjugkDJz8PYglSW4PXlsKNObRyiyBjrjAz75eejT5EiffPtUF-4sTTJsy8kDMbBvaZ0Ur0Fb5vDQRGatXUsIACUJ9oolCMunB1C~NR51a7bSPSzq~65x~E6RtCB~6tYDuyWfoTDcNtyu9F37bC-uIOpzPZ6gfdxUKWPGpY97F9em9EKeEHNBpI~8ZzDTAVSuPXBBuAa5Vo8zEpYx0gI0dh0sSj5imMJWAcemHnFw7J-~Jj~NujQQmEo7p590xGg__&Key-Pair-Id=K2RFTOXRBNSROX')

with col3:
    st.write('Liza Fontaine')
    st.image('https://i.pinimg.com/originals/5e/d5/51/5ed551c23dc3e12a63834346bface63e.jpg')