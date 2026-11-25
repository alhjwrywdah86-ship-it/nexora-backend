from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.db.session import get_db
from app.models.user import User

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
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return service.create_goal(
        db,
        current_user.id,
        data
    )
