!pip install streamlit --quiet
!pip install pyngrok --quiet

%%writefile app.py
import streamlit as st
st.write('# Hello World')
st.write('## Run Streamlit on Colab')
