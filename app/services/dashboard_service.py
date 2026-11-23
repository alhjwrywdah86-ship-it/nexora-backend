from app.repositories.goal_repository import (
    GoalRepository
)

from app.repositories.task_repository import (
    TaskRepository
)


class DashboardService:

    def __init__(self):

        self.goal_repo = GoalRepository()
        self.task_repo = TaskRepository()

    def get_dashboard(
        self,
        db,
        user_id
    ):

        goals = self.goal_repo.get_by_user(
            db,
            user_id
        )

        active_goals = len(goals)

        completed_tasks = 0
        pending_tasks = 0

        for goal in goals:

            tasks = self.task_repo.get_by_goal(
                db,
                goal.id
            )

            completed_tasks += len(
                [
                    t for t in tasks
                    if t.status == "completed"
                ]
            )

            pending_tasks += len(
                [
                    t for t in tasks
                    if t.status != "completed"
                ]
            )

        total = completed_tasks + pending_tasks

        progress = 0

        if total > 0:

            progress = int(
                (completed_tasks / total) * 100
            )

        streak = self.calculate_streak(
            completed_tasks
        )

        coach = self.generate_coach_message(
            progress,
            streak
        )

        return {
            "active_goals": active_goals,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "progress": progress,
            "current_streak": streak,
            "coach_message": coach
        }

    def calculate_streak(
        self,
        completed
    ):

        return min(
            completed,
            30
        )

    def generate_coach_message(
        self,
        progress,
        streak
    ):

        if streak >= 7:
            return (
                "🔥 أداء ممتاز! "
                "استمر في بناء عادات النجاح."
            )

        if progress >= 70:
            return (
                "🚀 أنت قريب من تحقيق هدفك."
            )

        if progress >= 30:
            return (
                "💡 تقدم جيد، استمر."
            )

        return (
            "⚡ ابدأ بمهمة واحدة اليوم."
      )
