from fastapi import APIRouter, HTTPException
from .models import User

router = APIRouter()

users = [
    User(id=1, user_id=1, user_infos="Yahya Aqrom;Male;23;Depok", alarm_sound="ring_1", notification_sound="ring_2", contacts="08976075402;08159045721"),
    User(id=2, user_id=2, user_infos="Yahya Aqrom;Male;23;Depok", alarm_sound="ring_1", notification_sound="ring_2", contacts="08976075402;08159045721"),
    User(id=3, user_id=3, user_infos="Yahya Aqrom;Male;23;Depok", alarm_sound="ring_1", notification_sound="ring_2", contacts="08976075402;08159045721"),
]

@router.get("/Users", tags=["Users"])
def get_all_users():
    if users:
        return users
    raise HTTPException(status_code=404, detail="No users found.")

@router.get("/Users/{user_id}", tags=["Users"])
def get_user_by_id(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found.")

@router.put("/Users/{user_id}", tags=["Users"])
def update_user_by_id(user_id: int, user: User):
    for u in users:
        if u.id == user_id:
            # Update the user information
            u.name = user.name
            u.email = user.email
            return {"message": "User updated successfully."}
    raise HTTPException(status_code=404, detail="User not found.")

@router.delete("/Users/{user_id}", tags=["Users"])
def delete_user_by_id(user_id: int):
    for i, user in enumerate(users):
        if user.id == user_id:
            del users[i]
            return {"message": "User deleted successfully."}
    raise HTTPException(status_code=404, detail="User not found.")

@router.post("/Users", tags=["Users"])
def create_user(user: User):
    users.append(user)
    return {"message": "User created successfully."}
