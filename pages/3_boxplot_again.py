## Box plot
import streamlit as st
import altair as alt
box = alt.Chart(stops).mark_boxplot().encode(
    x = alt.X('Was_a_Search_Conducted'),
    y = alt.Y('Driver_Age')
).properties(
    width = 500,
    title = 'Boxplot between Search Conducted vs Driver Age')

st.altair_chart(box)