from datetime import datetime
from pydantic import BaseModel

class VibrationHealth(BaseModel):
    id: int
    timestamp: datetime
    device_id: int
    health_category: str
    health_score: int