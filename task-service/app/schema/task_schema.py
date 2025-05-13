from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):
    user_id: int
    title: Optional[str]
    description: Optional[str]
    created_by: Optional[str]
    due_date: Optional[datetime]

class TaskRead(TaskCreate):
    id: int
    is_completed: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
