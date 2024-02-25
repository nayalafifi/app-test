%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import hvplot.pandas

import streamlit as st
backgroundColor = "#add8e6"
st.title("2022 World Cup Stats")
st.header("An analysis on the 2022 world cup")
st.image("messi.jpg")

st.radio('Pick your favorite team',['Argentina','Brazil','France','Germany','Morocco','Spain'])
st.selectbox('Pick your player of the tournament',['Messi','Mbappe','Ronaldo','Neymar','Hakimi','Di Maria','Bellingham','Modric'])
st.select_slider('How would you rate this tournament? ', ['Bad', 'Good', 'Excellent'])

df = pd.read_csv('2022worldcup.csv')
















# import altair as alt

# df = pd.DataFrame(
#    np.random.randn(500, 3),
#    columns=['x','y','z'])

# c = alt.Chart(df).mark_circle().encode(
#    x='x' , y='y' , size='z', color='z', tooltip=['x', 'y', 'z'])
# st.altair_chart(c, use_container_width=True)

# import seaborn as sns
# sampled_df = df.sample(n=1000)
# sampled_df_10_columns = sampled_df.iloc[:, :10]
# sns.pairplot(sampled_df_10_columns)
