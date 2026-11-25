import os

os.environ.setdefault("JWT_SECRET", "test-secret-test-secret-test-secret")
os.environ.setdefault("DATABASE_URL", "sqlite://")

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.db.base import Base
from app.db.session import get_db
from app.main import app
import app.models.user  # noqa: F401
import app.models.goal  # noqa: F401
import app.models.task  # noqa: F401


@pytest.fixture()
def client():

    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    Base.metadata.create_all(engine)

    TestingSession = sessionmaker(bind=engine)

    def override_get_db():
        db = TestingSession()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)

    app.dependency_overrides.clear()


@pytest.fixture()
def auth_headers(client):

    user = {
        "name": "Test",
        "email": "test@example.com",
        "password": "password123",
    }

    client.post("/auth/register", json=user)

    res = client.post(
        "/auth/login",
        json={
            "email": user["email"],
            "password": user["password"],
        },
    )

    return {
        "Authorization": f"Bearer {res.json()['access_token']}"
    }
