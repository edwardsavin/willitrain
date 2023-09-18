import pytest
import re
from project import get_rain_forecast, format_rain_forecast


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


def test_valid_rain_forecast():
    forecast = get_rain_forecast("London", "metric")

    assert isinstance(forecast, list)
    assert isinstance(forecast[0][0], dict)
    assert "temperature" in forecast[0][0]
    assert "weather_description" in forecast[0][0]
