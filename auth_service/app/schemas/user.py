from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]

class UserCreate(UserBase):
    password: str  # Plain password input

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserInDB(UserBase):
    id: int
    hashed_password: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        # This allows Pydantic to work with SQLAlchemy models
        # by converting them to dictionaries.