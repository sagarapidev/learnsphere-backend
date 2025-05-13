# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
from pydantic_settings import BaseSettings
from urllib.parse import quote_plus

class Settings(BaseSettings):
    DB_DRIVER: str
    DB_SERVER: str
    DB_PORT: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    @property
    def DATABASE_URL(self) -> str:
        odbc_str = (
            f"DRIVER={self.DB_DRIVER};"
            f"SERVER={self.DB_SERVER},{self.DB_PORT};"
            f"DATABASE={self.DB_NAME};"
            f"UID={self.DB_USER};"
            f"PWD={self.DB_PASSWORD}"
        )
        return f"mssql+pyodbc:///?odbc_connect={quote_plus(odbc_str)}"

    class Config:
        env_file = ".env"

settings = Settings()
# This code is a configuration module for a Python application that uses Pydantic to manage settings.
# It defines a Settings class that reads database connection parameters from environment variables and constructs a database URL.