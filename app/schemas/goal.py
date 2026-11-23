from pydantic import BaseModel


class GoalCreate(BaseModel):

    title: str
    description: str | None = None
    deadline: str | None = None


class GoalResponse(BaseModel):

    id: str
    title: str
    description: str | None
    deadline: str | None
    status: str
    progress: int
