import streamlit as st
import plotly.express as px
from backend import get_data
st.title("Weather Forecast for Next Days")
station = st.text_input("Fill Station")

days = st.slider("Forecast Days", min_value=1, max_value=5)

view = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{view} for next {days} days in {station}")

datas = get_data(station, days)


figure = px.line(x=date, y=temperature, labels={'x': 'date', 'y': 'temperature'})
st.plotly_chart(figure)
