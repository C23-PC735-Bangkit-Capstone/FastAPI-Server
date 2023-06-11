from pydantic import BaseModel

class Pond(BaseModel):
    id: int
    pond_id: int
    user_id: int
    pond_location: str