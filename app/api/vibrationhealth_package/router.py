from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy import text
from sqlalchemy.orm import Session
from .schemas import VibrationHealth as VibrationHealthSchema
from app.models import VibrationHealth as VibrationHealthModel
from app.database import get_db

router = APIRouter()

@router.get("/vibrationhealth", response_model=List[VibrationHealthSchema], tags=["Vibration Health"])
def get_all_vibration_health(db: Session = Depends(get_db)):
    vibration_health = db.query(VibrationHealthModel).all()
    return vibration_health

@router.post("/vibrationhealth", response_model=List[VibrationHealthSchema], tags=["Vibration Health"])
def create_vibration_health(vibration_health: VibrationHealthSchema, db: Session = Depends(get_db)):
    db_vibration_health = VibrationHealthModel(**vibration_health.dict())
    db.add(db_vibration_health)
    db.commit()
    db.refresh(db_vibration_health)
    return [vibration_health]

@router.get("/vibrationhealth/{device_id}", response_model=List[VibrationHealthSchema], tags=["Vibration Health"])
def get_vibration_health_by_device_id(device_id: int, db: Session = Depends(get_db)):
    vibration_health = db.query(VibrationHealthModel).filter(VibrationHealthModel.device_id == device_id).all()
    if not vibration_health:
        raise HTTPException(status_code=404, detail="Vibration health data not found for the device ID")
    return vibration_health

@router.get("/vibrationhealth/{device_id}/{date}", response_model=List[VibrationHealthSchema], tags=["Vibration Health"])
def get_vibration_health_by_device_id_and_date(device_id: int, date: str, db: Session = Depends(get_db)):
    query = text(
        "SELECT * FROM vibration_health WHERE device_id = :device_id "
        "AND CAST(timestamp AS DATE) = :date"
    )
    vibration_health = db.execute(query, {"device_id": device_id, "date": date}).fetchall()
    if not vibration_health:
        raise HTTPException(status_code=404, detail="Vibration health data not found for the device ID and date")
    return vibration_health