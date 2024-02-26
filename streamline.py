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

## Description of Dataset

num = st.number_input('No of Rows',5,10)
st.dataframe(df.head(num))

### Description of the dataset

st.dataframe(df.describe())

if st.button("Show Describe Code"):
        code = '''df.describe()'''
        st.code(code, language='python')

if st.button("Generate Report"):
  import streamlit as st
  import streamlit.components.v1 as components


st.markdown("## Visualization")

tab1, tab2 = st.tabs(["Line Chart", "Bar Chart"])

tab1.subheader("Line Chart")
# Display a line chart for the selected variables
tab1.line_chart(data=df, x="energy", y="popularity", width=0, height=0, use_container_width=True)

tab2.subheader("Bar Chart")
# Display a bar chart for the selected variables
tab2.bar_chart(data=df, x="energy", y="popularity", use_container_width=True)

fig, ax = plt.subplots()
sns.distplot(df['popularity'], ax=ax)
st.pyplot(fig)

# Correlation Heatmap of Audio Features
audio_features = df[['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'valence']]
audio_correlation = audio_features.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(audio_correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Audio Features')
st.pyplot(fig) 

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




