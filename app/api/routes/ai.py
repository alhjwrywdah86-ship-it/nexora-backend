from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field

from app.agents.execution_engine import (
    ExecutionEngine
)
from app.core.deps import get_current_user
from app.models.user import User


router = APIRouter()

engine = ExecutionEngine()


class PlanRequest(BaseModel):

    goal: str = Field(min_length=3, max_length=500)


@router.post("/ai/plan")
async def generate_plan(
    data: PlanRequest,
    current_user: User = Depends(get_current_user)
):

    return await engine.build_plan(
        data.goal
    )
