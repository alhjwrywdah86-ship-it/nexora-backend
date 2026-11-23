import uuid

from sqlalchemy import (
    Column,
    String
)

from app.db.base import Base


class Task(Base):

    __tablename__ = "tasks"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    goal_id = Column(
        String,
        nullable=False
    )

    title = Column(
        String(255),
        nullable=False
    )

    description = Column(
        String,
        nullable=True
    )

    status = Column(
        String,
        default="pending"
    )

    due_date = Column(
        String,
        nullable=True
    )

    completed_at = Column(
        String,
        nullable=True
    )
