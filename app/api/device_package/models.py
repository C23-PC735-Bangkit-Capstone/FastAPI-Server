from pydantic import BaseModel

class Device(BaseModel):
    id: int
    device_id:int
    pond_id: int
    signal_strength: int
    battery_strength: int
    condition: str