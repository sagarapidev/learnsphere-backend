from abc import ABC, abstractmethod
from typing import List
from app.schema.task_schema import TaskCreate, TaskRead

class ITaskService(ABC):
    @abstractmethod
    def get_all_tasks(self) -> List[TaskRead]:
        pass

    @abstractmethod
    def create_task(self, task_data: TaskCreate) -> TaskRead:
        pass
