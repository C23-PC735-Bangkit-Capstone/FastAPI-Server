from sqlalchemy import Column, DateTime, Integer, String
from sqladmin import ModelView
from .database import Base

class VibrationHealth(Base):
    __tablename__ = 'vibration_health'

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    device_id = Column(Integer, nullable=False)
    health_category = Column(String(30), nullable=False)
    health_score = Column(Integer, nullable=False)

class VibrationHealthAdmin(ModelView, model=VibrationHealth):
    column_list = [VibrationHealth.id, VibrationHealth.timestamp, VibrationHealth.device_id, VibrationHealth.health_category, VibrationHealth.health_score]