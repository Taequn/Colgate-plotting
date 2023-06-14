import streamlit as st
import pandas as pd
from plotnine import *
from plots.timeseries import make_major_timeseries

st.set_page_config(
    page_title="Majors Enrolled",
    page_icon="📈",
)

# Load data
@st.cache_data
def load_data():
    main_df = pd.read_csv("processed_data/enrolled_majors.csv")
    return main_df

data = load_data()

#for CLASSES take unique values of subject
CLASSES = data['subject'].unique()


# Sidebar
selected_classes = st.sidebar.multiselect('Select classes', CLASSES)


st.title('Number of Enrolled Majors')
st.write("This plot shows the number of students taking Senior Seminar or Senior Project in each year.")
st.write("If the line is flat, it means that no students took the class that year, or that the class was not offered that year.")
p = make_major_timeseries(data, selected_classes)

if len(selected_classes) > 0:
    st.pyplot(p.draw(p))
else:
    st.warning("Please select at least one class.")
