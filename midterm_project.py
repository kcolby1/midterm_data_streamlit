import csv
import pandas as pd
import streamlit as st
import altair as alt
import numpy as np

st.header('Midterm Project')

st.markdown(
"**MIDTERM PROJECT** My midterm project was based on Incident Reports filed in Boston MA 2021.\n"
"2021 was selected as the time period because this was the last full year on record."
)

st.code(
    '''
    # Read the CSV file into streamlit app
    # midterm_df = pd.read_csv(file name)''',language='csv')

midterm_df= pd.read_csv('midterm_data.csv')
st.write(midterm_df)

bar= alt.Chart(midterm_df).mark_bar(color= '#c7293b').encode(
    alt.X("DISTRICT", bin=True,title= "Police District"),
    alt.Y('count()',title="Incidents")
)
st.altair_chart(bar, use_container_width=True)

st.markdown(
    "This bar chart specifically for crime rports versus weekday"
)
bar= alt.Chart(midterm_df).mark_bar(color= '#692f36').encode(
    alt.X("DAY_OF_THE_WEEK", bin=True,title= "Day of the Week"),
    alt.Y('count()',title="Incident Reports")
)

shooting= st.selectbox(
    'Did the incident involve a shooting?'
    midterm_df['SHOOTING']
)
'You chose :', shooting