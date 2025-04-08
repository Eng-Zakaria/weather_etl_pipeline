import os
from pathlib import Path
from dotenv import load_dotenv

# Force load .env from project root
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    # Debugging - print all environment variables
    print("\nLoaded environment variables:")
    for k, v in os.environ.items():
        if k.startswith(('DB_', 'WEATHER_')):
            print(f"{k}: {v}")

    # Database Configuration
    DB_TYPE = os.getenv("DB_TYPE", "sqlite").lower().strip()
    
    if DB_TYPE == "sqlite":
        data_dir = Path(__file__).parent.parent / "data"
        data_dir.mkdir(exist_ok=True, mode=0o755)
        DB_URL = f"sqlite:///{data_dir}/weather.db"
    elif DB_TYPE == "postgres":
        DB_URL = (
            f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
            f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
        )
    else:
        raise ValueError(f"Unsupported database type: {DB_TYPE}")

    # Print final DB_URL for verification
    print(f"\nFinal DB_URL: {DB_URL}\n")

settings = Settings()