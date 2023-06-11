from datetime import datetime
from pydantic import BaseModel

class VibrationHealthBase(BaseModel):
    timestamp: datetime
    device_id: int
    health_category: str
    health_score: int

class VibrationHealthCreate(VibrationHealthBase):
    pass

class VibrationHealth(VibrationHealthBase):
    vibrationhealth_id: int
    time_created: datetime

    class Config:
        orm_mode = True
