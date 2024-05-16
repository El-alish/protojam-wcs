import streamlit as st
import pandas as pd
import numpy as np
import time
import streamlit.components.v1 as components
import plotly.express as px
import plotly.graph_objects as go  # for 3D plot visualization

from wordcloud import WordCloud
from langdetect import detect
from datetime import datetime
import plotly.figure_factory as ff

st.header('Répartition du traffic internet en France, Mars 2024', divider='rainbow')
tab1, tab2 = st.tabs(["Internet en France", "Classement par catégorie"])


with st.sidebar:
    #st.image('https://media4.giphy.com/media/PqcBU8T4SeuO3kOMVu/giphy.gif?cid=ecf05e47ayiowxuub1416x1q3ttwa8hrcpfhbje9g2ivq1m1&ep=v1_gifs_related&rid=giphy.gif&ct=g')
    st.image('https://cdn.discordapp.com/attachments/1210594061346672687/1240680856251531425/Designer_2.jpeg?ex=66477196&is=66462016&hm=e3ca395793ea5a222f3e435c5ad402ad2da2ac848b448384a441ccfe357b5947&')
df = pd.read_csv('pages/bidon.csv', sep=',')
#st.dataframe(df, use_container_width=True, hide_index=True)
with tab1:
    st.write("Sur les 15 sites les plus visités en Mars 2024 en France, 2 sites sont des sites lié à la culture Japonaise cumulant 257 Millions de visites en un mois")
    # Sort the dataframe by popularity and select the top 15
    top_10_popular = df.sort_values(by='Visites', ascending=False).head(15)
    
    # Create a bar chart with different colors for each bar
    fig3 = px.bar(top_10_popular, x='Visites', y='Domaine',
                            title='Top 15 des sites les plus visités en Mars 2024 en France',
                 color='Domaine',
                 width=800, height=800)
    fig3.update_layout(showlegend=False)
    # Note:- Less the popularity no. is more popular is the anime.
    
    st.plotly_chart(fig3, use_container_width=False)

with tab2:
    st.write("Sur les 15 sites les plus visités en Mars 2024 en France, 2 sites sont des sites lié à la culture Japonaise cumulant 257 Millions de visites en un mois")
    # Sort the dataframe by popularity and select the top 15
    top_10_popular = df.sort_values(by='Description catégorie', ascending=False).head(15)
    
    # Create a bar chart with different colors for each bar
    fig3 = px.bar(top_10_popular, x='Visites', y='Catégories',
                            title='Top 15 des catégories les plus visités en Mars 2024 en France',
                 color = 'Catégories',
                 width=800, height=800)
    fig3.update_layout(showlegend=False)
    # Note:- Less the popularity no. is more popular is the anime.
    
    st.plotly_chart(fig3, use_container_width=False)
