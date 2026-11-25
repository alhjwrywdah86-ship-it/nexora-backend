from datetime import datetime

from pydantic import BaseModel, Field


class GoalCreate(BaseModel):

    title: str = Field(min_length=1, max_length=255)
    description: str | None = None
    deadline: datetime | None = None


class GoalResponse(BaseModel):

    id: str
    title: str
    description: str | None
    deadline: datetime | None
    status: str
    progress: int
