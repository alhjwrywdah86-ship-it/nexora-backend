from app.models.goal import Goal
from app.models.task import Task


class TaskRepository:

    def create(
        self,
        db,
        task
    ):
        db.add(task)
        db.commit()
        db.refresh(task)

        return task

    def get_by_goal(
        self,
        db,
        goal_id
    ):
        return (
            db.query(Task)
            .filter(
                Task.goal_id == goal_id
            )
            .all()
        )

    def get_by_id(
        self,
        db,
        task_id
    ):
        return (
            db.query(Task)
            .filter(
                Task.id == task_id
            )
            .first()
        )

    def get_by_id_for_user(
        self,
        db,
        task_id,
        user_id
    ):
        """يرجع المهمة فقط إذا كانت تابعة لهدف يملكه المستخدم."""

        return (
            db.query(Task)
            .join(Goal, Goal.id == Task.goal_id)
            .filter(
                Task.id == task_id,
                Goal.user_id == user_id
            )
            .first()
        )
