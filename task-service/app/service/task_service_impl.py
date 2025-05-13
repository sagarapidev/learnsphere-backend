from typing import List
from sqlalchemy.orm import Session
from app.service.itask_service import ITaskService
from app.model.task_model import Task
from app.schema.task_schema import TaskCreate, TaskRead

class TaskServiceImpl(ITaskService):
    def __init__(self, db: Session):
        self.db = db

    def get_all_tasks(self) -> List[TaskRead]:
        return self.db.query(Task).all()

    def create_task(self, task_data: TaskCreate) -> Task:
        task = Task(**task_data.model_dump())
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task
