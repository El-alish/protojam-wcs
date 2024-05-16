import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
from langdetect import detect
from datetime import datetime


st.set_page_config(layout="wide")
st.header('Des graphiques', divider='rainbow')
with st.sidebar:
    #st.image('https://media4.giphy.com/media/PqcBU8T4SeuO3kOMVu/giphy.gif?cid=ecf05e47ayiowxuub1416x1q3ttwa8hrcpfhbje9g2ivq1m1&ep=v1_gifs_related&rid=giphy.gif&ct=g')
    st.image('https://cdn.discordapp.com/attachments/1210594061346672687/1240680856251531425/Designer_2.jpeg?ex=66477196&is=66462016&hm=e3ca395793ea5a222f3e435c5ad402ad2da2ac848b448384a441ccfe357b5947&')
df = pd.read_csv('https://github.com/El-alish/protojam-wcs/blob/main/anime-filtered.csv', sep=',')

#st.dataframe(df, use_container_width=True, hide_index=True, column_order=['Name', 'Score', 'English Name', 'Type', 'Episodes', 'Ranked', 'Rating', 'Genres.1'])
# Count the number of anime titles by type
type_counts = df['Type'].value_counts()

# Create a bar chart
fig = px.bar(type_counts, x=type_counts.index, y=type_counts.values, color=type_counts.index, labels={'x':'Anime Type', 'y':'Count'}, 
             title='Support des visionnages par type d\'anime')



st.plotly_chart(fig, use_container_width=True)


# Filter out anime titles with popularity value 0
df_valid_popularity = df[df['Popularity'] > 0]

# Sort the dataframe by popularity and select the top 15
top_10_popular = df_valid_popularity.sort_values(by='Popularity', ascending=True).head(15)

# Create a bar chart with different colors for each bar
fig3 = px.bar(top_10_popular, x='Name', y='Popularity',
             labels={'Name': 'Anime Title', 'Popularity': 'Popularity'},
             title='Top 15 Anime les plus populaires',
             color='Name')
# Note:- Less the popularity no. is more popular is the anime.

st.plotly_chart(fig3, use_container_width=True)

# Concatenate all genre values into a single string
genre_text = ' '.join(df[df['Genres.1'] != "UNKNOWN"]['Genres.1'].dropna())

# Create a WordCloud object
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(genre_text)

# Convert the WordCloud object to an image
wordcloud_image = wordcloud.to_image()

# Create a Plotly figure to display the WordCloud image
fig4 = go.Figure(go.Image(z=wordcloud_image))
fig4.update_layout(title='Nuage de mots')


st.plotly_chart(fig4, use_container_width=True)

# Function to extract the season and year from the premiered string
def extract_season_year(premiered):
    if premiered == 'UNKNOWN':
        return None, None
    else:
        season = premiered.split()
        return season

# Apply the function to extract the season and year from the "Premiered" column
season_year = df['Premiered'].map(extract_season_year)
premiered_season = season_year.apply(lambda x: x[0])
premiered_Year = season_year.apply(lambda x: x[0])

# Filter out None values from premiered_season
filtered_premiered_season = premiered_season.dropna()

# Count the occurrences of each season
season_counts = filtered_premiered_season.value_counts()

# Create the pie plot
fig5 = go.Figure(data=go.Pie(
    labels=season_counts.index,
    values=season_counts.values,
    hole=0.4,  # Add a donut hole in the center
    hoverinfo='label+percent',  # Display label and percentage on hover
    textinfo='value',  # Display count value as text inside each slice
    textfont=dict(size=14),  # Set the text font size
    marker=dict(
        colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'],  # Custom color palette
        line=dict(color='#ffffff', width=2)  # Set the color and width of the slice borders
    )
))

# Set the title and font style for the plot
fig5.update_layout(
    title='Sortie suivant les saisons',
    title_font=dict(size=20),
    font=dict(size=12, color='#555555')
)

fig5.show()

st.plotly_chart(fig5, use_container_width=True)

df_user = pd.read_csv('Protojam/user-filtered.csv', sep=';')

# Distribution of gender
# Count the occurrences of each gender
gender_counts = df_user['gender'].value_counts(dropna=True)

# Define custom colors for the pie slices
colors = ['rgb(0, 123, 255)', 'rgb(255, 65, 54)', 'rgb(255, 187, 0)', 'rgb(125, 125, 125)']

# Create the pie plot
fig6 = go.Figure()

fig6.add_trace(go.Pie(
    labels=gender_counts.index,
    values=gender_counts.values,
    hole=0.3,
    marker=dict(colors=colors, line=dict(color='#FFFFFF', width=2)),
    hoverinfo='label+percent',
    hovertemplate='<b>%{label}</b><br>%{percent}',
    textinfo='value',
    textposition='inside',
    sort=False
))

# Customize the layout
fig6.update_layout(
    title='Répartition des genres des utilisateurs',
    title_x=0.5,
    uniformtext_minsize=12,
    uniformtext_mode='hide',
    showlegend=False,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=20, r=20, t=100, b=20),
)

st.plotly_chart(fig6, use_container_width=True)
