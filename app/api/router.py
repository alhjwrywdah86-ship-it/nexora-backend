from fastapi import APIRouter

from app.api.routes.health import router as health_router


api_router = APIRouter()

api_router.include_router(
    health_router,
    tags=["Health"]
)
from app.api.routes.auth import (
    router as auth_router
)

api_router.include_router(
    auth_router,
    tags=["Auth"]
)
from app.api.routes.goals import (
    router as goals_router
)

from app.api.routes.tasks import (
    router as tasks_router
)

api_router.include_router(
    goals_router,
    tags=["Goals"]
)

api_router.include_router(
    tasks_router,
    tags=["Tasks"]
)
from app.api.routes.dashboard import (
    router as dashboard_router
)

api_router.include_router(
    dashboard_router,
    tags=["Dashboard"]
)
from app.api.routes.ai import (
    router as ai_router
)

api_router.include_router(
    ai_router,
    tags=["AI"]
)
