from configparser import ConfigParser
import sys


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


def main():
    ...


if __name__ == "__main__":
    main()
