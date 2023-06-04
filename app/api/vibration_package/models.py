from datetime import datetime
from pydantic import BaseModel

class Vibration(BaseModel):
    id: int
    timestamp: datetime
    device_id: int
    accx: float
    accy: float
    accz: float