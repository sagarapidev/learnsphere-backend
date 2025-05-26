from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL") or ""
    # Alternatively, raise an error if not set:
    # DATABASE_URL: str = os.getenv("DATABASE_URL")
    # if DATABASE_URL is None:
    #     raise ValueError("DATABASE_URL environment variable is not set")

settings = Settings()
