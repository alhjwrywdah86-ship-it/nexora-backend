from fastapi import APIRouter

from app.agents.execution_engine import (
    ExecutionEngine
)


router = APIRouter()

engine = ExecutionEngine()


@router.post("/ai/plan")
async def generate_plan(
    goal: str
):

    return await engine.build_plan(
        goal
    )
