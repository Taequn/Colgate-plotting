import streamlit as st
import pandas as pd
from plotnine import *
from plots.timeseries import make_timeseries, make_entrollment_timeseries

st.set_page_config(
    page_title="Enrollment and Classes Offered",
    page_icon="📚",
)

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

if timeseries_type == 'Classes Offered':
    st.title('Number of Offered Classes')
    st.write("This plot shows the number of classes offered in each semester.")
    p = make_timeseries(data, selected_classes)
else:
    st.title('Number of Enrolled Students')
    st.write("This plot shows the number of enrolled students in each semester.")
    p = make_entrollment_timeseries(data, selected_classes)

if len(selected_classes) > 0:
    st.pyplot(p.draw(p))
else:
    st.warning("Please select at least one class.")
