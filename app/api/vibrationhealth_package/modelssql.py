# from datetime import datetime
# from pydantic import BaseModel
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqladmin import ModelView

Base = declarative_base()

class VibrationHealth(Base):
    __tablename__ = 'vibration_health'

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    device_id = Column(Integer)
    health_category = Column(String)
    health_score = Column(Integer)

class VibrationHealthAdmin(ModelView, model=VibrationHealth):
    column_list = [VibrationHealth.id, VibrationHealth.timestamp, VibrationHealth.device_id, VibrationHealth.health_category, VibrationHealth.health_score]