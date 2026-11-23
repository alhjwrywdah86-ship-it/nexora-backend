from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.user import (
    UserRegister,
    UserLogin
)

from app.services.auth_service import (
    AuthService
)

from app.db.session import get_db


router = APIRouter()

service = AuthService()


@router.post("/auth/register")
def register(
    data: UserRegister,
    db: Session = Depends(get_db)
):
    return service.register(
        db,
        data
    )


@router.post("/auth/login")
def login(
    data: UserLogin,
    db: Session = Depends(get_db)
):
    return service.login(
        db,
        data
    )
