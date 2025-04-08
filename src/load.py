from sqlalchemy import create_engine, Table, Column, MetaData
from sqlalchemy import Float, String, Date, Integer
import pandas as pd
from config import settings

def get_database_engine():
    """Create database connection"""
    return create_engine(settings.settings.DB_URL)

def ensure_weather_table(engine):
    """Create table if not exists"""
    metadata = MetaData()
    
    weather_table = Table(
        'weather', metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('date', Date, nullable=False, unique=True),
        Column('avg_temp', Float),
        Column('max_temp', Float),
        Column('min_temp', Float),
        Column('avg_humidity', Float),
        Column('total_precipitation', Float),
        Column('temp_range', Float)
    )
    
    metadata.create_all(engine)
    return weather_table

def load_weather_data(df: pd.DataFrame):
    """Load transformed data to database"""
    engine = get_database_engine()
    ensure_weather_table(engine)
    
    df.to_sql(
        'weather',
        engine,
        if_exists='append',
        index=False,
        method='multi'
    )