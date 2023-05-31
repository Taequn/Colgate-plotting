import streamlit as st
import pandas as pd
from plotnine import *
from timeseries import make_timeseries

# Load data
@st.cache_data
def load_data():
    main_df = pd.read_csv("processed_data/data.csv")
    return main_df

data = load_data()

#for CLASSES take unique values of subject
CLASSES = data['subject'].unique()

# Sidebar
selected_classes = st.sidebar.multiselect('Select classes', CLASSES)

st.title("Time Series Plot")

p = make_timeseries(data, selected_classes)
if len(selected_classes) > 0:
    st.pyplot(p.draw(p))
else:
    st.write("Please select at least one class.")
