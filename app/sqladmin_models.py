from sqlalchemy import Column, DateTime, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Device(Base):
    __tablename__ = 'device'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    device_id = Column(Integer, nullable=False)
    pond_id = Column(Integer, nullable=False)
    signal_strength = Column(Integer, nullable=False)
    battery_strength = Column(Integer, nullable=False)
    condition = Column(String(30), nullable=False)

class Pond(Base):
    __tablename__ = 'pond'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pond_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    pond_location = Column(String(30), nullable=False)

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    user_infos = Column(String(30), nullable=False)
    alarm_sound = Column(String(30), nullable=False)
    notification_sound = Column(String(30), nullable=False)
    contacts = Column(String(30), nullable=False)

class Vibration(Base):
    __tablename__ = 'vibration'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    timestamp = Column(DateTime, nullable=False)
    device_id = Column(Integer, nullable=False)
    accx = Column(Float, nullable=False)
    accy = Column(Float, nullable=False)
    accz = Column(Float, nullable=False)

class VibrationHealth(Base):
    __tablename__ = 'vibration_health'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    timestamp = Column(DateTime, nullable=False)
    device_id = Column(Integer, nullable=False)
    health_category = Column(String(30), nullable=False)
    health_score = Column(Integer, nullable=False)