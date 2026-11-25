from fastapi import HTTPException, status

from app.models.user import User
from app.repositories.user_repository import UserRepository

from app.core.security import (
    hash_password,
    verify_password
)

from app.core.jwt import (
    create_access_token
)


class AuthService:

    def __init__(self):

        self.repo = UserRepository()

    def register(
        self,
        db,
        data
    ):

        email = data.email.lower()

        existing = self.repo.get_by_email(
            db,
            email
        )

        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already exists"
            )

        user = User(
            name=data.name,
            email=email,
            password_hash=hash_password(
                data.password
            )
        )

        return self.repo.create(
            db,
            user
        )

    def login(
        self,
        db,
        data
    ):

        user = self.repo.get_by_email(
            db,
            data.email.lower()
        )

        if (
            not user
            or not user.is_active
            or not verify_password(
                data.password,
                user.password_hash
            )
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        return {
            "access_token": create_access_token(
                user.id
            ),
            "token_type": "bearer"
            }
