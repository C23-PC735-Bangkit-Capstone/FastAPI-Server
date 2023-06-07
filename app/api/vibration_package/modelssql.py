# from sqlalchemy.orm import Model
from sqlalchemy import Column, DateTime, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqladmin import ModelView

Base = declarative_base()

class Vibration(Base):
    __tablename__ = 'vibration'

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    device_id = Column(Integer)
    accx = Column(Float)
    accy = Column(Float)
    accz = Column(Float)

class VibrationAdmin(ModelView, model=Vibration):
    column_list = [Vibration.id, Vibration.timestamp, Vibration.device_id, Vibration.accx, Vibration.accy, Vibration.accz]