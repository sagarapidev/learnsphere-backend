from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app.config.db_config import Base
from sqlalchemy.sql import func

class Task(Base):
    __tablename__ = "Tasks"
    __table_args__ = {"schema": "lsb"}

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    title = Column(String(100))
    description = Column(String)
    created_by = Column(String(50))
    due_date = Column(DateTime)
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
