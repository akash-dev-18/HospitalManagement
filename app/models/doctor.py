from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import ForeignKey, String, Integer


from app.db import Base
from app.models.user import User


class Doctor(Base):
    __tablename__ = "doctors"
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id"), nullable=False
    )
    specialization: Mapped[str] = mapped_column(String(100), nullable=False)
    license_no: Mapped[str] = mapped_column(String(12), nullable=False)

    user: Mapped[User | None] = relationship(
        back_populates="doctor", uselist=False, cascade="all,delete-orphan"
    )
    department: Mapped[Department] = relationship(
        back_populates="doctors", cascade="all,delete-orphan"
    )

    appointments: Mapped[list[Appointment]] = relationship(
        back_populates="doctor", cascade="all ,delete-orphan"
    )
    medical_records: Mapped[list[MedicalRecord]] = relationship(
        back_populates="doctor", cascade="all ,delete-orphan"
    )
