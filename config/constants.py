# API Configuration
OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"
DEFAULT_LOCATION = {
    "latitude": 40.7128,  # NYC
    "longitude": -74.0060,
    "timezone": "America/New_York"
}

# Weather Parameters
DAILY_WEATHER_VARIABLES = [
    "temperature_2m_max",
    "temperature_2m_min",
    "temperature_2m_mean",
    "precipitation_sum",
    "relative_humidity_2m_mean"
]