import streamlit as st
st.write ('this is page1')

import pandas as pd
from plotly import express as px
data = pd.read_csv('banking.csv')


st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Charts"])

if page == "Home":
    st.title("Welcome to the Banking Data Analysis App")
    st.write("""
    This app provides interactive visualizations of banking data.
    Navigate to the "Charts" page to explore interactive graphs.
    """)
    st.dataframe(data.head())
elif page == "Charts":
    st.title("Interactive Charts")
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Distribution of Age")
        age_range = st.slider("Select Age Range", int(data['age'].min()), int(data['age'].max()), (20, 50))
        filtered_data = data[(data['age'] >= age_range[0]) & (data['age'] <= age_range[1])]
        fig1 = px.histogram(filtered_data, x="age", title="Age Distribution", nbins=20)
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("Age vs. Balance")
        fig2 = px.scatter(data, x="age", y="duration", title="How long they used the apps", color="job")
        st.plotly_chart(fig2, use_container_width=True)