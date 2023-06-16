from datetime import datetime
from pydantic import BaseModel, conlist

class Vibration(BaseModel):
    timestamp: datetime
    device_id: int
    accx: float
    accy: float
    accz: float

    class Config:
        orm_mode = True

class VibrationUnit(BaseModel):
    Timestamp: str
    AccX: str
    AccY: str
    AccZ: str

class VibrationPackage(BaseModel):
    device_id: int
    data: conlist(VibrationUnit, min_items=1)

    class Config:
        orm_mode = True