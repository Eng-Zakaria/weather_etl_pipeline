# Weather ETL Pipeline 🌤️

A modular pipeline for extracting, transforming, and loading weather data from the Open-Meteo API(https://open-meteo.com).

## Features

- **API Data Extraction**: Fetch historical weather data
- **Data Transformation**: Calculate derived metrics (temp range, etc.)
- **Database Loading**: Supports SQLite (default) and PostgreSQL
- **CLI Interface**: Configurable days/location via command line

## Project Structure

```plaintext
.
├── config/              # Configuration files
│   ├── constants.py     # API parameters
│   └── settings.py      # DB connection settings
├── data/                # SQLite database storage
├── src/
│   ├── extract.py       # API data fetching
│   ├── transform.py     # Data processing
│   ├── load.py          # Database operations
│   ├── main.py          # Pipeline orchestration
│   └── fetch_weather.py # CLI entrypoint
└── tests/               # Unit tests
```

## Installation

```bash
git clone https://github.com/Eng-Zakaria/weather_etl_pipeline
cd weather_etl_pipeline
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## Configuration

Edit `.env` file:

```ini
# For SQLite (default):
DB_TYPE=sqlite

# For PostgreSQL:
DB_TYPE=postgres
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=weather
```

## Usage

**Command Line:**
```bash
# Fetch last 7 days for NYC (default)
python src/fetch_weather.py

# Custom location and timeframe
python src/fetch_weather.py --days 14 --lat 51.5074 --long -0.1278
```

**Programmatic:**
```python
from src.main import run_pipeline

# Fetch 10 days for London
run_pipeline(days=10, location={
    "latitude": 51.5074,
    "longitude": -0.1278,
    "timezone": "Europe/London"
})
```

## Tech Stack

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-orange)](https://sqlalchemy.org)
[![Pandas](https://img.shields.io/badge/Pandas-1.5%2B-green)](https://pandas.pydata.org)
- **Extract**: `requests`
- **Transform**: `pandas`
- **Load**: `sqlalchemy`

## Testing

```bash
pytest tests/
```

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

## License

MIT License - See LICENSE(LICENSE) for details