from fastapi import Depends, FastAPI, Response, status, APIRouter, HTTPException
from sqlalchemy.orm import Session
from .schemas import VibrationHealthCreate
from .models import VibrationHealth
from app.database import get_db, SessionLocal

router = APIRouter()

@router.get("/", tags=["Test DB"])
def check_db(db: SessionLocal = Depends(get_db)):
    print("Database session:", db) 
    return {"status": "Database connection successful"}

@router.get("/VibrationHealth/{device_id}", tags=["Vibration Health"])
def get_vibration_health_by_device_id(device_id: int, db=Depends(get_db)):
    result = db.query(VibrationHealth).filter(VibrationHealth.device_id == device_id).all()
    if result:
        return result
    raise HTTPException(status_code=404, detail="No vibration health data found for the provided DeviceId.")

@router.get("/VibrationHealth/{device_id}/{date}", tags=["Vibration Health"])
def get_vibration_health_by_device_id_and_date(device_id: int, date: str, db=Depends(get_db)):
    result = db.query(VibrationHealth).filter(VibrationHealth.device_id == device_id, VibrationHealth.timestamp.date() == date).all()
    if result:
        return result
    raise HTTPException(status_code=404, detail="No vibration health data found for the provided DeviceId and Date.")

@router.post("/VibrationHealth", tags=["Vibration Health"], status_code=201)
def create_vibration_health(vibration_health: VibrationHealthCreate, db=Depends(get_db)):
    db_vibration_health = VibrationHealth(
        timestamp=vibration_health.timestamp,
        device_id=vibration_health.device_id,
        health_category=vibration_health.health_category,
        health_score=vibration_health.health_score
    )
    db.add(db_vibration_health)
    db.commit()
    db.refresh(db_vibration_health)
    return {"message": "Vibration health data created successfully."}
