from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Integer, ForeignKey, Date

from datetime import date

from app.db import Base
from app.models.user import User


class Patient(Base):
    __tablename__ = "patients"
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), unique=True, nullable=False
    )
    blood_group: Mapped[str | None] = mapped_column(String(5), nullable=True)
    dob: Mapped[date | None] = mapped_column(Date, nullable=True)
    phone: Mapped[str | None] = mapped_column(String(20), nullable=True)
    address: Mapped[str | None] = mapped_column(String(100), nullable=True)

    # relationship
    patient: Mapped[User | None] = relationship(
        back_populates="patient", uselist=False, cascade="all ,delete-orphan"
    )
