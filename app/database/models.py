import datetime
from typing import Annotated

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship

Base = declarative_base()
intpk = Annotated[int, mapped_column(primary_key=True)]


class UserOrm(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    name: Mapped[str]
    gender: Mapped[str]
    age: Mapped[int]

    heart_rate: Mapped[list["HeartRateOrm"]] = relationship(back_populates="user")


class HeartRateOrm(Base):
    __tablename__ = "heart_rates"

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), index=True)
    timestamp: Mapped[datetime.datetime]
    heart_rate: Mapped[float]

    user: Mapped["UserOrm"] = relationship(back_populates="heart_rate")
