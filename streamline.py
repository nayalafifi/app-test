pip install streamlit --quiet
pip install pyngrok --quiet
import pandas as pd
import numpy as np
import seaborn as sns
import hvplot.pandas
import streamlit as st
backgroundColor = "#add8e6"
st.title ("2022 World Cup Stats")
st.header("An analysis on the 2022 world cup")
st.image("messi.jpg")

st.radio('Pick your favorite team',['Argentina','Brazil','France','Germany','Morocco','Spain'])
st.selectbox('Pick your player of the tournament',['Messi','Mbappe','Ronaldo','Neymar','Hakimi','Di Maria','Bellingham','Modric'])
st.select_slider('How would you rate this tournament? ', ['Bad', 'Good', 'Excellent'])

df = pd.read_csv('2022worldcup.csv')
