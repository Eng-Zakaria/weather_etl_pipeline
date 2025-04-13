# API Configuration
from typing import Dict, List

API_BASE_URL: str = "https://api.open-meteo.com/v1/forecast"
DEFAULT_LOCATION: Dict[str, float | str] = {
    "latitude": 40.7128,  # NYC
    "longitude": -74.0060,
    "timezone": "America/New_York"
}

# Weather Parameters
DAILY_WEATHER_VARIABLES: List[str] = [
    "temperature_2m_max",
    "temperature_2m_min",
    "temperature_2m_mean",
    "precipitation_sum",
    "relative_humidity_2m_mean"
]