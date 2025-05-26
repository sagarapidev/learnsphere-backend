from sqlalchemy import Column, Integer, String,DateTime, func
from app.infrastructure.database.connection import Base

class User(Base):
    __tablename__ = "Users"
    __table_args__ = {"schema": "lsb"}  # Use schema if needed

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=True)
    email = Column(String(100), nullable=True)
    hashed_password = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
