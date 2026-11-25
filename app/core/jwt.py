from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt

from app.core.config import settings


ALGORITHM = "HS256"


def create_access_token(
    user_id: str,
    expires_minutes: int = 30
):

    expire = datetime.now(timezone.utc) + timedelta(
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


def decode_access_token(token: str):
    """يرجع user_id أو None إذا كان التوكن غير صالح."""

    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[ALGORITHM]
        )
    except JWTError:
        return None

    return payload.get("sub")
