import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import hvplot.pandas
import streamlit as st
backgroundColor = "#add8e6"
st.title("Netflix TV Shows and Movies")
st.header("An analysis on the IMBD Scores")
st.image(taylor-swift-eras-tour-032023-1-e1f1db4f3659494d9f40b35cc53736ca.jpg)

st.radio('What is your favorite genre?',['Comedy','Drama','Mystery','Crime'])
# st.selectbox('Pick your player of the tournament',['Messi','Mbappe','Ronaldo','Neymar','Hakimi','Di Maria','Bellingham','Modric'])
# st.select_slider('How would you rate this tournament? ', ['Bad', 'Good', 'Excellent'])

df = pd.read_csv('taylor_swift_spotify.csv')
df.head()
df.columns

fig, ax = plt.subplots()
sns.distplot(df['popularity'], ax=ax)
st.pyplot(fig)

# Correlation Heatmap of Audio Features
audio_features = df[['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'valence']]
audio_correlation = audio_features.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(audio_correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Audio Features')
st.pyplot() 

# Top Most Popular Albums
top_albums = df.groupby('album')['popularity'].mean().sort_values(ascending=False).head(10)

# Reverse the order of the DataFrame
top_albums = top_albums[::-1]

fig, ax = plt.subplots()
top_albums.plot(kind='barh', color='skyblue', ax=ax) 
plt.title('Top Albums by Popularity')
plt.xlabel('Average Popularity')  
plt.ylabel('Album')  
st.pyplot(fig)





