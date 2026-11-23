from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.schemas.goal import (
    GoalCreate
)

from app.services.goal_service import (
    GoalService
)


router = APIRouter()

service = GoalService()


@router.post("/goals")
def create_goal(
    data: GoalCreate,
    db: Session = Depends(get_db)
):

    user_id = "demo-user"

    return service.create_goal(
        db,
        user_id,
        data
  )
