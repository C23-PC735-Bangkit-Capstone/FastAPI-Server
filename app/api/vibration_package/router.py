from csv import reader
from fastapi import Depends, File, APIRouter, HTTPException, UploadFile
from typing import List
from sqlalchemy import text
from sqlalchemy.orm import Session
from .schemas import Vibration as VibrationSchema
from app.models import Vibration as VibrationModel
from app.database import get_db
import json

router = APIRouter()

@router.post("/vibrations", tags=["Vibration"])
async def create_vibration_data_from_json(file: UploadFile = File(...)):
    contents = await file.read().decode("utf-8")
    try:
        # Try parsing the contents as JSON
        data = json.loads(contents)
    except json.JSONDecodeError:
        # If parsing as JSON fails, parse as a nested array
        csv_data = reader(contents.splitlines())
        data = list(csv_data)
    print(data)
    return data

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