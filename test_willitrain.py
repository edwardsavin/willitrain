import pytest
import re
from willitrain import get_rain_forecast, format_rain_forecast, get_random_city


def test_invalid_units():
    with pytest.raises(SystemExit) as e:
        get_rain_forecast("London", "invalid")

    assert e.type == SystemExit
    assert e.value.code == "Invalid units. Please use either metric or imperial."


def test_invalid_location():
    with pytest.raises(SystemExit) as e:
        get_rain_forecast("Bad Location 333", "random")

    assert e.type == SystemExit
    assert e.value.code == (
        "Sorry but I couldn't find that location. To make the search more precise, please put the "
        "city's name, comma, 2-letter country code (ISO3166)."
    )


def test_random_units():
    forecast = get_rain_forecast("London", "random")
    formatted_forecast = format_rain_forecast(forecast)
    units_regex = r"\| \d+°[C|F] \|"

    assert re.search(units_regex, formatted_forecast[0]) is not None


def test_get_rain_forecast():
    forecast = get_rain_forecast("London", "metric")

    assert isinstance(forecast, list)
    assert isinstance(forecast[0][0], dict)
    assert "temperature" in forecast[0][0]
    assert "weather_description" in forecast[0][0]


def test_format_rain_forecast():
    forecast = get_rain_forecast("London", "metric")
    formatted_forecast = format_rain_forecast(forecast)

    assert isinstance(formatted_forecast, list)
    assert isinstance(formatted_forecast[0], str)
    assert "|" in formatted_forecast[0]


def test_get_random_city():
    city = get_random_city()

    assert isinstance(city, str)
