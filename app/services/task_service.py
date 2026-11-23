from datetime import datetime

from app.repositories.task_repository import (
    TaskRepository
)


class TaskService:

    def __init__(self):

        self.repo = TaskRepository()


    def complete_task(
        self,
        db,
        task
    ):

        task.status = "completed"

        task.completed_at = str(
            datetime.utcnow()
        )

        db.commit()

        return task


    def calculate_progress(
        self,
        tasks
    ):

        if not tasks:
            return 0

        completed = len(
            [
                t for t in tasks
                if t.status == "completed"
            ]
        )

        return int(
            completed
            / len(tasks)
            * 100
        )
