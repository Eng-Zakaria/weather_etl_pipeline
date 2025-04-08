from .extract import fetch_weather_data
from .transform import transform_weather_data
from .load import load_weather_data

def run_pipeline(days: int = 7):
    """Run complete ETL pipeline"""
    # Extract
    raw_data = fetch_weather_data(days=days)
    
    # Transform
    df = transform_weather_data(raw_data)
    
    # Load
    load_weather_data(df)
    print(f"Successfully loaded {len(df)} records")

if __name__ == "__main__":
    run_pipeline()