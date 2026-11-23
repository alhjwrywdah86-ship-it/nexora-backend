import uuid

from sqlalchemy import (
    Column,
    String,
    Integer
)

from app.db.base import Base


class Goal(Base):

    __tablename__ = "goals"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    user_id = Column(
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

    deadline = Column(
        String,
        nullable=True
    )

    status = Column(
        String,
        default="active"
    )

    progress = Column(
        Integer,
        default=0
    )
