import streamlit as st

st.set_page_config(
    page_title="test"
)

st.markdown ('#This is the main page...')
st.sidebar.write('main page')

import pandas as pd
df = pd.read_csv('banking.csv')
st.dataframe(df)