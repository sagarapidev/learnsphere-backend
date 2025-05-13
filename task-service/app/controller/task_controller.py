from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.db_config import SessionLocal
from app.service.task_service_impl import TaskServiceImpl
from app.schema.task_schema import TaskCreate, TaskRead
from typing import List

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[TaskRead])
def get_tasks(db: Session = Depends(get_db)):
    return TaskServiceImpl(db).get_all_tasks()

@router.post("/", response_model=TaskRead)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return TaskServiceImpl(db).create_task(task)
