# Add proper error handling
from sqlalchemy.engine import URL

class Settings:
    def __init__(self):
        self._load_db_config()
    
    def _load_db_config(self):
        self.DB_TYPE = os.getenv("DB_TYPE", "sqlite").lower().strip()
        
        if self.DB_TYPE == "sqlite":
            self._configure_sqlite()
        elif self.DB_TYPE == "postgres":
            self._configure_postgres()
        else:
            raise ValueError(f"Unsupported DB type: {self.DB_TYPE}")

    def _configure_sqlite(self):
        data_dir = Path(__file__).parent.parent / "data"
        data_dir.mkdir(exist_ok=True, mode=0o755)
        self.DB_URL = f"sqlite:///{data_dir}/weather.db"

    def _configure_postgres(self):
        self.DB_URL = URL.create(
            drivername="postgresql",
            username=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_NAME")
        )