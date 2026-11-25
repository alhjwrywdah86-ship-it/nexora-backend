import os

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


def _required(name: str) -> str:
    value = os.getenv(name)

    if not value or value == "CHANGE_ME":
        raise RuntimeError(
            f"المتغير {name} غير مضبوط في البيئة"
        )

    return value


class Settings(BaseModel):

    APP_NAME: str = "NEXORA AI"
    APP_VERSION: str = "0.1.0"

    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://nexora:nexora@localhost:5432/nexora"
    )

    REDIS_URL: str = os.getenv(
        "REDIS_URL",
        "redis://localhost:6379"
    )

    JWT_SECRET: str = _required("JWT_SECRET")

    DB_ECHO: bool = os.getenv("DB_ECHO", "false").lower() == "true"

    CORS_ORIGINS: list[str] = [
        origin.strip()
        for origin in os.getenv("CORS_ORIGINS", "").split(",")
        if origin.strip()
    ]


settings = Settings()
