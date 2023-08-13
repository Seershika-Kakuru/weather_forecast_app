import streamlit as st
import plotly.express as px
from data_finder import get_data

# Getting all the required data from the user
st.title("Weather Forecast for the Next Days:")
place = st.text_input("Please enter a place: ")
nr_of_days = st.slider("Please choose the number of days: ", min_value=1, max_value=5)
kind = st.selectbox("Select data to view: ", options=["Temperature", "Sky"])

try:
    # Making sure a valid place is entered
    if place:
        # Getting the weather data for a given number of days as a:
        # list of dictionaries
        # there are 8 times the number of days dictionaries
        # corresponding to the weather for every 3 hours for 'nr_of_days'
        required_dictionaries = get_data(place, nr_of_days)
        # getting the dates and times for (8 * nr_of_days) intervals
        dates = [dict['dt_txt'] for dict in required_dictionaries]
        # Displaying the subheader
        st.subheader(f"{kind} for the next {nr_of_days} days in {place}:")
        if kind == "Temperature":
            # Extracting temperatures from the 'required_dictionaries'
            temperatures = [dict['main']['temp'] for dict in required_dictionaries]
            # Creating a plotly line graph
            plotly_figure = px.line(x=dates, y=temperatures,
                                    labels={'x': "Date", 'y': "Temperature in °C"},
                                    markers=True,
                                    hover_name=temperatures)
            # Passing on the plotly figure to streamlit's plotly_chart method
            st.plotly_chart(plotly_figure)
        if kind == "Sky":
            # Extracting sky conditions from the 'required_dictionaries'
            sky_conditions = [dict['weather'][0]['main'] for dict in required_dictionaries]
            # Creating a dictionary with paths to respective images
            weather_images = {"Clouds": "images/cloud.png", "Clear": "images/clear.png",
                              "Rain": "images/rain.png", "Snow": "images/snow.png"}
            # Generating a list of image paths for each condition in sky_conditions
            images_to_be_displayed = [weather_images[condition] for condition in sky_conditions]
            st.image(image=images_to_be_displayed, caption=dates, width=115)
except KeyError:
    # Warning if a valid place is not entered
    st.warning("Please enter a valid place!!")





