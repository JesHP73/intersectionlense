#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def show_page(df):
    st.title("Air Pollution Impact Analysis")
    st.write("Analyze the impact of air pollution across different demographics.")

    # Filters
    selected_region = st.sidebar.multiselect('Select Region', options=df['region'].unique())
    selected_country = st.sidebar.multiselect('Select Country', options=df['country'].unique())
    selected_zone = st.sidebar.multiselect('Select Zone', options=df['zone'].unique())

    # Data filtering
    filtered_data = df[
        df['region'].isin(selected_region) &
        df['country'].isin(selected_country) &
        df['zone'].isin(selected_zone)
    ]

    # Plotting
    fig, ax = plt.subplots()
    sns.barplot(x='air_pollutant', y='avg_air_pollutant_level', hue='age_group', data=filtered_data, ax=ax)
    st.pyplot(fig)

