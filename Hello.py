#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import gni_aqi_analysis
import trends_over_time
import pollution_impact

# Function to load data
@st.cache
def load_data():
    DATA_URL = 'https://raw.githubusercontent.com/JesHP73/IntersectionalClimateLense/82562b5a84f5af80373d79691b331ed0c33843ea/data_sets/socio_economical_agg_dataset.csv'
    data = pd.read_csv(DATA_URL)
    return data

# Load data
df = load_data()

# Page configuration
st.set_page_config(page_title="Intersectional Climate Trends", layout="wide")

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a Page", ["GNI vs AQI Analysis", "Trends Over Time", "Air Pollution Impact Analysis"])

if page == "GNI vs AQI Analysis":
    gni_aqi_analysis.show_page(df)
elif page == "Trends Over Time":
    trends_over_time.show_page(df)
elif page == "Air Pollution Impact Analysis":
    pollution_impact.show_page(df)

