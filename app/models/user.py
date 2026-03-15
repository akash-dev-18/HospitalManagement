from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Integer

import enum

from app.db import Base
from app.models.patient import Patient


class RoleEnum(enum.Enum):
    admin = "admin"
    doctor = "doctor"
    patient = "patient"


class User(Base):
    __tablename__ = "users"
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
    )
    role: Mapped[RoleEnum] = mapped_column(String(20), nullable=False)

    # relationships
    patient: Mapped[Patient | None] = relationship(
        back_populates="user", uselist=False, cascade="all, delete-orphan"
    )
