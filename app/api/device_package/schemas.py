from pydantic import BaseModel

class Device(BaseModel):
    device_id:int
    pond_id: int
    signal_strength: int
    battery_strength: int
    condition: str

    class Config:
        orm_mode = True