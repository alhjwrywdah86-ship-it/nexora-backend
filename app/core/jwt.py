from datetime import datetime, timedelta

from jose import jwt

from app.core.config import settings


ALGORITHM = "HS256"


def create_access_token(
    user_id: str,
    expires_minutes: int = 30
):

    expire = datetime.utcnow() + timedelta(
        minutes=expires_minutes
    )

    payload = {
        "sub": user_id,
        "exp": expire
    }

    return jwt.encode(
        payload,
        settings.JWT_SECRET,
        algorithm=ALGORITHM
    )
