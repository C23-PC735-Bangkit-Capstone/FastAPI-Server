from datetime import datetime
from pydantic import BaseModel

class Vibration(BaseModel):
    timestamp: datetime
    device_id: int
    accx: float
    accy: float
    accz: float

    class Config:
        orm_mode = True