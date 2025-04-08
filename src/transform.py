import pandas as pd

def transform_weather_data(raw_data: dict) -> pd.DataFrame:
    """Convert API response to structured DataFrame"""
    daily = raw_data.get('daily', {})
    
    df = pd.DataFrame({
        'date': pd.to_datetime(daily['time']),
        'max_temp': daily['temperature_2m_max'],
        'min_temp': daily['temperature_2m_min'],
        'avg_temp': daily['temperature_2m_mean'],
        'total_precipitation': daily['precipitation_sum'],
        'avg_humidity': daily['relative_humidity_2m_mean']
    })
    
    # Derived fields
    df['temp_range'] = df['max_temp'] - df['min_temp']
    df['date'] = df['date'].dt.date
    
    return df