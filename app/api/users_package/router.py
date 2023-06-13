from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .schemas import Users as UserSchema
from app.models import Users as UserModel
from app.database import get_db

router = APIRouter()

@router.get("/users", response_model=List[UserSchema], tags=["Users"])
def get_all_users(db: Session = Depends(get_db)):
    user = db.query(UserModel).all()
    if not user:
        raise HTTPException(status_code=404, detail="User data not found")
    return user

@router.post("/users", response_model=List[UserSchema], tags=["Users"])
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    db_user = UserModel(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return [user]

@router.delete("/users", response_model=List[UserSchema], tags=["Users"])
def delete_all_users(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    if not users:
        raise HTTPException(status_code=404, detail="User not found.")
    for user in users:
        db.delete(user)
    db.commit()
    return users

@router.get("/users/{user_id}", response_model=List[UserSchema], tags=["Users"])
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    users = db.query(UserModel).filter(UserModel.user_id == user_id).all()
    if not users:
        raise HTTPException(status_code=404, detail="User data not found for the user ID")
    return users

@router.put("/users/{user_id}", response_model=UserSchema, tags=["Users"])
def update_user_by_id(user_id: int, updated_user: UserSchema, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User data not found for the user ID")
    for attr, value in updated_user.dict(exclude_unset=True).items():
        setattr(user, attr, value)
    db.commit()
    db.refresh(user)
    return user

@router.delete("/users/{user_id}", response_model=UserSchema, tags=["Users"])
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    db.delete(user)
    db.commit()
    return user
