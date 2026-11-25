from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.core.deps import get_current_user
from app.db.session import get_db
from app.models.user import User

from app.services.dashboard_service import (
    DashboardService
)


router = APIRouter()

service = DashboardService()


@router.get("/dashboard")
def dashboard(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    return service.get_dashboard(
        db,
        current_user.id
    )
