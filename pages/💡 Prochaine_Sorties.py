import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app

st.set_page_config(layout="wide")
with st.sidebar:
    #st.image('https://media4.giphy.com/media/PqcBU8T4SeuO3kOMVu/giphy.gif?cid=ecf05e47ayiowxuub1416x1q3ttwa8hrcpfhbje9g2ivq1m1&ep=v1_gifs_related&rid=giphy.gif&ct=g')
    st.image('https://cdn.discordapp.com/attachments/1210594061346672687/1240680856251531425/Designer_2.jpeg?ex=66477196&is=66462016&hm=e3ca395793ea5a222f3e435c5ad402ad2da2ac848b448384a441ccfe357b5947&')

st.header('Prochaine Sorties Animes', divider='rainbow')
st.write('Tableau interactif')

components.iframe('https://anichart.net/Spring-2024', height=1300)