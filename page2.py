import streamlit as st
st.write ('this is page2')

from PIL import Image
im = Image.open('shrdc_logo.png')
st.image(im, width=300)