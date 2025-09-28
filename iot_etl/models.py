from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import Float, Integer, DateTime, UniqueConstraint, func

Base = declarative_base()

class IOTData(Base):
    __tablename__ = 'iot_tbl'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime)
    temperature: Mapped[float] = mapped_column(Float)
    humidity: Mapped[float] = mapped_column(Float)
    atmospheric_pressure: Mapped[float] = mapped_column(Float)
    gas: Mapped[float] = mapped_column(Float)
    wind_speed: Mapped[float] = mapped_column(Float)
    precipitation: Mapped[float] = mapped_column(Float)
    wind_direction: Mapped[float] = mapped_column(Float)
    uv: Mapped[float] = mapped_column(Float)

    __table_args__ = (
        UniqueConstraint('created_at', name='uq_created_at'),
    )