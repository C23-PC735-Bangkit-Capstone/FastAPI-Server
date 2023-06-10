from sqlalchemy import Column, DateTime, Integer, String
from .database import Base

class VibrationHealth(Base):
    __tablename__ = 'vibration_health'

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    device_id = Column(Integer, nullable=False)
    health_category = Column(String(30), nullable=False)
    health_score = Column(Integer, nullable=False)