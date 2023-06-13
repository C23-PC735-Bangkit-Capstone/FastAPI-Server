from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .schemas import Pond as PondSchema
from app.models import Pond as PondModel
from app.database import get_db


from fastapi import APIRouter, HTTPException
from .schemas import Pond

router = APIRouter()

@router.get("/ponds", response_model=List[PondSchema], tags=["Pond"])
def get_all_ponds(db: Session = Depends(get_db)):
    ponds = db.query(PondModel).all()
    if not ponds:
        raise HTTPException(status_code=404, detail="Pond data not found")
    return ponds

@router.post("/ponds", response_model=List[PondSchema], tags=["Pond"])
def create_pond(pond: PondSchema, db: Session = Depends(get_db)):
    db_pond = PondModel(**pond.dict())
    db.add(db_pond)
    db.commit()
    db.refresh(db_pond)
    return [pond]

@router.get("/ponds/{user_id}", response_model=List[PondSchema], tags=["Pond"])
def get_ponds_by_user_id(user_id: int, db: Session = Depends(get_db)):
    ponds = db.query(PondModel).filter(PondModel.user_id == user_id).all()
    if not ponds:
        raise HTTPException(status_code=404, detail="Pond data not found for the user ID")
    return ponds

@router.get("/ponds/pond/{pond_id}", response_model=List[PondSchema], tags=["Pond"])
def get_pond_by_id(pond_id: int, db: Session = Depends(get_db)):
    ponds = db.query(PondModel).filter(PondModel.pond_id == pond_id).all()
    if not ponds:
        raise HTTPException(status_code=404, detail="Pond data not found for the pond ID")
    return ponds

@router.put("/ponds/{pond_id}", response_model=PondSchema, tags=["Pond"])
def update_pond_by_id(pond_id: int, updated_pond: PondSchema, db: Session = Depends(get_db)):
    pond = db.query(PondModel).filter(PondModel.pond_id == pond_id).first()
    if not pond:
        raise HTTPException(status_code=404, detail="Pond data not found for the pond ID")
    for attr, value in updated_pond.dict(exclude_unset=True).items():
        setattr(pond, attr, value)
    db.commit()
    db.refresh(pond)
    return pond

@router.delete("/ponds/{pond_id}", response_model=PondSchema, tags=["Pond"])
def delete_pond_by_id(pond_id: int, db: Session = Depends(get_db)):
    pond = db.query(PondModel).filter(PondModel.pond_id == pond_id).first()
    if not pond:
        raise HTTPException(status_code=404, detail="Pond not found.")
    db.delete(pond)
    db.commit()
    return pond