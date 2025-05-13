from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# This code sets up the SQLAlchemy database engine and session for a FastAPI application.
# It creates a session factory (SessionLocal) and a declarative base class (Base) for defining ORM models.