import requests


def get_data(place, nr_of_days=None):
    # The URL points to weather data for the next five days with 3 hours intervals
    API_key = "4e5db0bf2e58b7b66a1b9f3051bd6d55"
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}&units=metric"
    # Getting a response object from url
    response = requests.get(url)
    # Extracting json data from the response object
    weather_dict = response.json()
    # returning the data for the requested number of days for the given place
    required_dictionaries = weather_dict['list'][0:(nr_of_days*8)]
    return required_dictionaries


if __name__ == "__main__":
    print(get_data("New York", 2))
