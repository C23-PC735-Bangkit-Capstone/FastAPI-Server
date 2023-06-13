from pydantic import BaseModel

class Device(BaseModel):
    device_id:int
    pond_id: int
    signal_strength: int
    battery_strength: int
    device_status: bool
    monitor_status: bool
    paddlewheel_condition: str

    class Config:
        orm_mode = True