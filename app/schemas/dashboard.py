from pydantic import BaseModel


class DashboardResponse(BaseModel):

    active_goals: int

    completed_tasks: int

    pending_tasks: int

    progress: int

    current_streak: int

    coach_message: str
