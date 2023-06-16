from datetime import datetime
from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy import text
from sqlalchemy.orm import Session
from .schemas import Vibration as VibrationSchema
from .schemas import VibrationPackage as VibrationPackageSchema
from app.models import Vibration as VibrationModel
from app.database import get_db

router = APIRouter()

@router.post("/vibrations", response_model=VibrationPackageSchema, tags=["Vibration"])
async def create_vibration_data(vibration: VibrationPackageSchema, db: Session = Depends(get_db)):
    for vibration_data in vibration.data:
        timestamp = datetime.fromtimestamp(int(vibration_data.Timestamp))
        accx = float(vibration_data.AccX)
        accy = float(vibration_data.AccY)
        accz = float(vibration_data.AccZ)
        print(timestamp, accx, accy, accz)
        vibration_instance = VibrationModel(
            timestamp=timestamp,
            device_id=vibration.device_id,
            accx=accx,
            accy=accy,
            accz=accz
        )
        db.add(vibration_instance)
    db.commit()
    db.refresh(vibration_instance)

    return vibration

@router.post("/vibration", response_model=List[VibrationSchema], tags=["Vibration"])
def create_vibration(vibration: VibrationSchema, db: Session = Depends(get_db)):
    db_vibration = VibrationModel(**vibration.dict())
    db.add(db_vibration)
    db.commit()
    db.refresh(db_vibration)
    return [vibration]

@router.get("/vibrations/{device_id}", response_model=List[VibrationSchema], tags=["Vibration"])
def get_vibrations_by_device_id(device_id: int, db: Session = Depends(get_db)):
    vibrations = db.query(VibrationModel).filter(VibrationModel.device_id == device_id).limit(100).all()
    if not vibrations:
        raise HTTPException(status_code=404, detail="Vibration data not found for the device ID")
    return vibrations

@router.get("/vibration/{device_id}/{date}", response_model=List[VibrationSchema], tags=["Vibration"])
def get_vibrations_by_device_id_and_date(device_id: int, date: str, db: Session = Depends(get_db)):
    query = text(
        "SELECT * FROM vibration WHERE device_id = :device_id "
        "AND CAST(timestamp AS DATE) = :date"
    )
    vibration = db.execute(query, {"device_id": device_id, "date": date}).fetchall()
    if not vibration:
        raise HTTPException(status_code=404, detail="Vibration data not found for the device ID and date")
    return vibration