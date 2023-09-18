from configparser import ConfigParser
from colorama import init, Fore
import sys
import requests
import datetime
import random
import argparse


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
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/forecast"


def main():
    """
    Get the rain forecast for the day and print it to the console

    It performs the following steps:
        1. Get the rain forecast for the day
        2. Format the rain forecast as a list of strings
        3. Print the rain forecast to the console

    Returns:
        None
    """

    arg_parser = argparse.ArgumentParser(
        prog="Will It Rain",
        description="Get the rain forecast for the day",
        epilog="Enjoy the rain! (...or not)",
    )
    arg_parser.add_argument(
        "location",
        nargs="?",
        type=str,
        help="The location to get the forecast for",
        default="Cluj-Napoca",  # TODO: implement getting location from IP
    )
    arg_parser.add_argument(
        "-u",
        "--units",
        type=str,
        help="The units to use for the forecast (metric or imperial)",
        default="metric",
    )
    args = arg_parser.parse_args()

    init(autoreset=True)
    forecast = get_rain_forecast(args.location, args.units)
    formatted_forecast = format_rain_forecast(forecast)

    print(f"Forecast for {args.location}:")
    for forecast in formatted_forecast:
        if "rain" in forecast.lower():
            print(Fore.BLUE + forecast)
        else:
            print(forecast)


def get_rain_forecast(location, units="metric"):
    """
    Get the rain forecast for the day

    Args:
        location (str): The location to get the forecast for
        units (str): The units to use for the forecast (metric or imperial)

    Returns:
        list: A list of dictionaries containing the hourly forecast data
    """

    if units not in ["metric", "imperial", "random"]:
        sys.exit("Invalid units. Please use either metric or imperial.")

    if units == "random":
        units = random.choice(["metric", "imperial"])

    request_url = f"{WEATHER_API_URL}?q={location}&units={units}&APPID={API_KEY}"

    try:
        response = requests.get(request_url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            sys.exit("Access denied. Please check your API key.")
        elif e.response.status_code == 404:
            sys.exit(
                "Sorry but I couldn't find that location. To make the search more precise, please put the city's name, "
                "comma, 2-letter country code (ISO3166)."
            )
        else:
            sys.exit(f"Sorry but something went wrong: {e.response.status_code}")

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
                    "temperature": int(round(forecast["main"]["temp"])),
                    "weather_description": forecast["weather"][0]["description"],
                }
            )

    return [hourly_forecast, units]


def format_rain_forecast(forecast):
    """
    Format the rain forecast for the day as a list of strings

    Args:
        forecast (list): A list containing the hourly forecast data

    Returns:
        list: A list of formatted forecast strings"""

    unit_symbols = {
        "metric": "°C",
        "imperial": "°F",
    }
    hourly_forecast, units = forecast
    unit = unit_symbols[units]

    formatted_forecast = []

    for f in hourly_forecast:
        formatted_forecast.append(
            f"{f['date_time']} | {f['temperature']}{unit} | {f['weather_description'].title()}"
        )

    return formatted_forecast


if __name__ == "__main__":
    main()
