from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy import text
from sqlalchemy.orm import Session
from .schemas import Vibration as VibrationSchema
from app.models import Vibration as VibrationModel
from app.database import get_db
import json

router = APIRouter()

@router.post("/vibrations/{device_id}", tags=["Vibration"])
async def create_vibration_data_from_stringified_json(data: str, device_id: int, db: Session = Depends(get_db)):
    nested_array = json.loads(data)

    for vibration_data in nested_array:
        vibration = VibrationSchema(timestamp=vibration_data[0], device_id=device_id, accx=vibration_data[1], accy=vibration_data[2], accz=vibration_data[3])
        db_vibration = VibrationModel(**vibration.dict())
        db.add(db_vibration)
        db.commit()
        db.refresh(db_vibration)

    return {"data": nested_array}

@router.post("/vibration", response_model=List[VibrationSchema], tags=["Vibration"])
def create_vibration(vibration: VibrationSchema, db: Session = Depends(get_db)):
    db_vibration = VibrationModel(**vibration.dict())
    db.add(db_vibration)
    db.commit()
    db.refresh(db_vibration)
    return [vibration]

@router.get("/vibration/{device_id}", response_model=List[VibrationSchema], tags=["Vibration"])
def get_vibrations_by_device_id(device_id: int, db: Session = Depends(get_db)):
    vibration = db.query(VibrationModel).filter(VibrationModel.device_id == device_id).all()
    if not vibration:
        raise HTTPException(status_code=404, detail="Vibration data not found for the device ID")
    return vibration

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