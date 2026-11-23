from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.services.dashboard_service import (
    DashboardService
)


router = APIRouter()

service = DashboardService()


@router.get("/dashboard")
def dashboard(
    db: Session = Depends(get_db)
):

    user_id = "demo-user"

    return service.get_dashboard(
        db,
        user_id
    )
