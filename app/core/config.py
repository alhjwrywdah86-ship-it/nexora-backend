from pydantic import BaseModel
import os


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

    JWT_SECRET: str = os.getenv(
        "JWT_SECRET",
        "CHANGE_ME"
    )


settings = Settings()
