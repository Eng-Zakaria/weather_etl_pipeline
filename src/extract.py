import requests
from datetime import datetime, timedelta
from config import constants

def fetch_weather_data(location: dict = None, days: int = 7) -> dict:
    """Fetch raw weather data from API"""
    params = {
        **(constants.DEFAULT_LOCATION if not location else location),
        "daily": constants.DAILY_WEATHER_VARIABLES,
        "temperature_unit": "fahrenheit",
        "start_date": (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d'),
        "end_date": datetime.now().strftime('%Y-%m-%d')
    }
    
    response = requests.get(constants.OPEN_METEO_URL, params=params)
    response.raise_for_status()
    return response.json()