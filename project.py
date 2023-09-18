from configparser import ConfigParser
import sys
import requests
import datetime


def _get_api_key():
    """
    Get the API key from the config file

    Expects a "secrets.ini" file in the same directory as this file with the following format:
        [openweather]
        api_key=<OPENWEATHER_API_KEY>

    Returns:
        str: The API key
    """

    config = ConfigParser()
    config.read("secrets.ini")
    return config["openweather"]["api_key"]


API_KEY = _get_api_key()
WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/forecast"


def main():
    forecast = get_rain_forecast("London", "metric")
    print_rain_forecast(forecast)


def get_rain_forecast(location, units="metric"):
    """
    Get the rain forecast for the day

    Args:
        location (str): The location to get the forecast for
        units (str): The units to use for the forecast (metric or imperial)

    Returns:
        list: A list of dictionaries containing the hourly forecast data
    """

    request_url = f"{WEATHER_API_URL}?q={location}&units={units}&APPID={API_KEY}"
    response = requests.get(request_url)
    data = response.json()

    hourly_forecast = []

    # Get the current date and convert it to a timestamp
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    timestamp = datetime.datetime.strptime(today, "%Y-%m-%d").timestamp()

    # Loop through the forecast data and filter hourly data for the desired date
    for forecast in data["list"]:
        if timestamp <= forecast["dt"] < timestamp + 86400:  # 86400 seconds in a day
            hourly_forecast.append(
                {
                    "date_time": datetime.datetime.utcfromtimestamp(
                        forecast["dt"]
                    ).strftime("%H:%M"),
                    "temperature": f"{int(round(forecast['main']['temp']))}°C",
                    "weather_description": forecast["weather"][0]["description"],
                }
            )

    return hourly_forecast


def print_rain_forecast(hourly_forecast):
    """
    Print the rain forecast for the day

    Args:
        hourly_forecast (list): A list of dictionaries containing the hourly forecast data

    Returns:
        None
    """

    for forecast in hourly_forecast:
        print(
            f"{forecast['date_time']} | {forecast['temperature']} | {forecast['weather_description'].title()}"
        )


if __name__ == "__main__":
    main()
