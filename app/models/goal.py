import uuid

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
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
        ForeignKey("users.id"),
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

    deadline = Column(
        DateTime(timezone=True),
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
