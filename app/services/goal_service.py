from app.models.goal import Goal

from app.agents.planner_agent import (
    PlannerAgent
)

from app.models.task import Task

from app.repositories.goal_repository import (
    GoalRepository
)

from app.repositories.task_repository import (
    TaskRepository
)


class GoalService:
    def __init__(self):
        self.planner = PlannerAgent()

    def __init__(self):

        self.goal_repo = GoalRepository()
        self.task_repo = TaskRepository()

    def create_goal(
        self,
        db,
        user_id,
        data
    ):

        goal = Goal(
            user_id=user_id,
            title=data.title,
            description=data.description,
            deadline=data.deadline
        )

        saved_goal = self.goal_repo.create(
            db,
            goal
        )

        tasks = self.generate_tasks(
            db,
            saved_goal
        )

        return {
            "goal": saved_goal,
            "tasks": tasks
        }

    def generate_tasks(self, db, goal):
        generated = self.planner.generate_plan(
            goal.title,
            goal.description
        )

        created_tasks = []

        for item in generated:
            task = Task(
                goal_id=goal.id,
                title=item["title"],
                description=item["description"]
            )
            saved = self.task_repo.create(
                db,
                task
            )
            created_tasks.append(saved)

        return created_tasks
