import streamlit as st
from PIL import Image


st.markdown("<h1 style='text-align: center; color: black;'>Analytics Project-HENRY DATA SCIENCE</h1>",
            unsafe_allow_html=True)

st.markdown("***")
image = Image.open('src/airplane-crash.jpg')
st.image(image)

st.markdown("<h2 style='text-align: center; color: black;'>By Angel Bello Merlo</h2>",
            unsafe_allow_html=True)


