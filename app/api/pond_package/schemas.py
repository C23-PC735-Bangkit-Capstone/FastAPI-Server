from pydantic import BaseModel

class Pond(BaseModel):
    pond_id: int
    user_id: int
    pond_location: str

    class Config:
        orm_mode = True