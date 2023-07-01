import streamlit as st
import plotly.express as px
from backend import get_data
st.title("Weather Forecast for Next Days")
station = st.text_input("Fill Station")

days = st.slider("Forecast Days", min_value=1, max_value=5)

view = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{view} for next {days} days in {station}")

if station:
    datas = get_data(station, days)
    if view == "Temperature":
        dates = [date["dt_txt"] for date in datas]
        temperature = [temper["main"]["temp"]/10 for temper in datas]
        figure = px.line(x=dates, y=temperature, labels={'x': 'Dates', 'y': 'Temperature'})
        st.plotly_chart(figure)
    if view == "Sky":
        file = {"Rain": "rain.png", "Clear": "clear.png", "Clouds": "cloud.png", "Snow": "snow.png"}
        weather_icon = [icon["weather"][0]["main"] for icon in datas]
        images_path = ["images/"+file[i] for i in weather_icon]
        dates = [date["dt_txt"] for date in datas]
        st.image(images_path, width=115, caption=dates)
