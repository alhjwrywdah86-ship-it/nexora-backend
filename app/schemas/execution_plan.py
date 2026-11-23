from pydantic import BaseModel


class ExecutionTask(BaseModel):

    title: str
    description: str
    priority: str


class ExecutionPlan(BaseModel):

    goal: str

    estimated_days: int

    tasks: list[ExecutionTask]
