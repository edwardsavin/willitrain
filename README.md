# willitrain
Final project for Harvard's CS50P

### Screenshot

![Will It Rain Screenshot](https://i.imgur.com/AuxQsdG.png)

### Overview

"Will It Rain" is a Python application that provides you with the rain forecast for the day in a specified location. It utilizes the OpenWeather API to fetch weather data and Geonames API to retrieve location information. You can easily check if it's going to rain today in your city or even explore the rain forecast in a random location.

### Features

- Get rain forecast for the day in a specific location.
- Choose between metric and imperial units for temperature.
- Check rain forecast in a random location for a bit of fun. 
- Automatically detects your city based on your IP address if no location is provided.

### Installation

1. Clone the repository:
```
git clone https://github.com/edwardsavin/willitrain.git
```

2. Install the required Python packages:
```
pip install -r requirements.txt
```

3. Create a secrets.ini file in the same directory as the script with the following format:
```
[openweather]
api_key=<YOUR_OPENWEATHER_API_KEY>

[geonames]
username=<YOUR_GEONAMES_USERNAME>
```
- Replace <YOUR_OPENWEATHER_API_KEY> with your OpenWeather API key. 
- Replace <YOUR_GEONAMES_USERNAME> with your Geonames username.

### Usage

```
python willitrain.py [location] [-u {metric,imperial,random}] [-rl]
```
- location (optional): The location to get the forecast for. If not provided, the app will attempt to detect your city based on your IP address.
- -u or --units (optional): Specify the units for the forecast. Options are metric (default), imperial, or random (randomly selects metric or imperial).
- -rl or --random-location (optional): Run Will It Rain on a random location.

### Example Usage

- Check the rain forecast for New York City in metric units:

```
python willitrain.py "New York, US"
```

- Check the rain forecast for a random location with random units:

```
python willitrain.py -rl
```

### Dependencies

- [OpenWeather API](https://openweathermap.org/api)
- [Geonames API](https://www.geonames.org/export/web-services.html)
- [argparse](https://docs.python.org/3/library/argparse.html): For parsing command line arguments.
- [geocoder](https://geocoder.readthedocs.io/): For IP-based city detection.
- [requests](https://docs.python-requests.org/en/latest/): For making HTTP requests to APIs.
- [colorama](https://pypi.org/project/colorama/): For colored console output.
- [configparser](https://docs.python.org/3/library/configparser.html): For reading API keys from secrets.ini.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Acknowledgements

- [Harvard University](https://pll.harvard.edu/course/cs50s-introduction-programming-python/): For the great course.
- [David J. Malan](https://cs.harvard.edu/malan/): For being an amazing lecturer.

Enjoy the rain forecast with "Will It Rain"! 🌧️
