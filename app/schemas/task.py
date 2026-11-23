from pydantic import BaseModel


class TaskCreate(BaseModel):

    title: str
    description: str | None = None


class TaskResponse(BaseModel):

    id: str
    title: str
    description: str | None
    status: str
