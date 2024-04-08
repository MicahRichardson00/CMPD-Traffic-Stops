import streamlit as st
import pandas as pd
import altair as alt

@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df
stops = load_data('data/Officer_Traffic_Stops.csv')
st.dataframe(stops)

age_bar = alt.Chart(stops).mark_bar().encode(
    alt.X("Driver_Age:Q", bin=True),
    y='count()',
)
st.altair_chart(age_bar)