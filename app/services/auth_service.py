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

        existing = self.repo.get_by_email(
            db,
            data.email
        )

        if existing:
            raise Exception(
                "Email already exists"
            )

        user = User(
            name=data.name,
            email=data.email,
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
            data.email
        )

        if not user:
            return None

        if not verify_password(
            data.password,
            user.password_hash
        ):
            return None

        return {
            "access_token":
                create_access_token(
                    user.id
                )
        }
