#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def show_page(df):
    st.title("Trends Over Time")
    st.write("Visualize the trends in Air Quality and Economic Development over different decades.")

    # Filters
    selected_metric = st.sidebar.selectbox('Select Metric', options=['avg_AQI_Index', 'avg_GNI_PPP', 'total_population'])
    selected_region = st.sidebar.multiselect('Select Region', options=df['region'].unique())

    # Data filtering
    filtered_data = df[df['region'].isin(selected_region)]

    # Plotting
    fig, ax = plt.subplots()
    sns.lineplot(x='decade', y=selected_metric, hue='region', data=filtered_data, ax=ax)
    st.pyplot(fig)

