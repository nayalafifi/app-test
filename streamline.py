import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Taylor Swift Spotify Popularity")
st.header("An analysis of popularity of Taylor Swift music")
st.image("taylor-swift-eras-tour-032023-1-e1f1db4f3659494d9f40b35cc53736ca.jpg")
st.header("This dataset consist of data from Spotify's API on all albums listed on Spotify for Taylor Swift.")

st.radio('What is your favorite album?',['reputation','1989','Folklore','Red','Fearless','Speak Now','evermore','Midnights'])
st.selectbox('Pick your favorite song',['Blank Space','Cardigan','Ready for it...?','Shake it Off','Red'])
st.select_slider('How would you rate her music? ', ['Bad', 'Meh', 'Good', 'Excellent'])

st.header("Now lets move to the analysis!")

# Create a sidebar header and a separator
st.sidebar.header("Dashboard")
st.sidebar.markdown("---")
                                        
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




