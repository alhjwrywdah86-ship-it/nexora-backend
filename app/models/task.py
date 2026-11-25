import uuid

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
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
        ForeignKey("goals.id"),
        nullable=False,
        index=True
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
        DateTime(timezone=True),
        nullable=True
    )

    completed_at = Column(
        DateTime(timezone=True),
        nullable=True
    )
