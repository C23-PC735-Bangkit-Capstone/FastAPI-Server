from pydantic import BaseModel

class Users(BaseModel):
    user_id: int
    user_infos: str
    alarm_sound: str
    notification_sound: str
    contacts: str

    class Config:
        orm_mode = True