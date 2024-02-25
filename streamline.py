import streamlit as st
import numpy as np
st.title ("2022 World Cup Stats")
st.header("An analysis on the 2022 world cup")
st.image("messi.jpg")

st.radio('Pick your favorite team',['Argentina','Brazil','France','Germany','Morocco','Spain'])
st.selectbox('Pick your sportr',['Basketball','Football'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])



