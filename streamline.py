import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.title ("2022 World Cup Stats")
st.header("An analysis on the 2022 world cup")
st.image("messi.jpg")

rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)
