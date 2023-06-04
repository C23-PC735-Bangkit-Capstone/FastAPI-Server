from pydantic import BaseModel

class User(BaseModel):
    id: int
    user_id: int
    user_infos: str
    alarm_sound: str
    notification_sound: str
    contacts: str