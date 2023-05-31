import streamlit as st
import pandas as pd
from plotnine import *
from timeseries import make_timeseries, make_entrollment_timeseries

# Load data
@st.cache_data
def load_data():
    main_df = pd.read_csv("processed_data/data.csv")
    return main_df

data = load_data()

#for CLASSES take unique values of subject
CLASSES = data['subject'].unique()



# Sidebar
timeseries_type = st.sidebar.radio(label="Choose the type of timeseries", options=['Enrollment', 'Classes Offered'])
selected_classes = st.sidebar.multiselect('Select classes', CLASSES)

st.title("Time Series Plot")

if timeseries_type == 'Classes Offered':
    p = make_timeseries(data, selected_classes)
else:
    p = make_entrollment_timeseries(data, selected_classes)


if len(selected_classes) > 0:
    st.pyplot(p.draw(p))
else:
    st.write("Please select at least one class.")
