#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def show_page(df):
    st.title("GNI vs AQI Analysis")
    st.write("Explore how Gross National Income (GNI) correlates with Air Quality Index (AQI) across different regions.")

    # Filters
    selected_region = st.sidebar.multiselect('Select Region', options=df['region'].unique())
    selected_country = st.sidebar.multiselect('Select Country', options=df['country'].unique())
    selected_decade = st.sidebar.multiselect('Select Decade', options=df['decade'].unique(), format_func=lambda x: str(x))
    selected_zone = st.sidebar.multiselect('Select Zone', options=df['zone'].unique())

    # Data filtering
    filtered_data = df[
        df['region'].isin(selected_region) &
        df['country'].isin(selected_country) &
        df['decade'].isin(selected_decade) &
        df['zone'].isin(selected_zone)
    ]

    # Plotting
    fig, ax = plt.subplots()
    sns.scatterplot(x='avg_GNI_PPP', y='avg_AQI_Index', hue='region', data=filtered_data, ax=ax)
    st.pyplot(fig)

