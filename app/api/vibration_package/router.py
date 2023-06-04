from fastapi import APIRouter, HTTPException
from .models import Vibration
from datetime import datetime

router = APIRouter()

vibrations = [
    Vibration(id=1, timestamp=datetime(2023, 1, 1, 23, 3, 20), device_id=1, accx=0.4, accy=3, accz=-7),
    Vibration(id=2, timestamp=datetime(2023, 1, 1, 23, 3, 20), device_id=1, accx=0.4, accy=3, accz=-7),
    Vibration(id=3, timestamp=datetime(2023, 1, 1, 23, 3, 20), device_id=2, accx=0.4, accy=3, accz=-7),
]

@router.get("/Vibrations/{device_id}")
def get_vibrations_by_device_id(device_id: int):
    result = [vibration for vibration in vibrations if vibration.device_id == device_id]
    if result:
        return result
    raise HTTPException(status_code=404, detail="No vibrations found for the provided DeviceId.")

@router.get("/Vibrations/{device_id}/{date}")
def get_vibrations_by_device_id_and_date(device_id: int, date: str):
    result = [vibration for vibration in vibrations if vibration.device_id == device_id and vibration.date == date]
    if result:
        return result
    raise HTTPException(status_code=404, detail="No vibrations found for the provided DeviceId and Date.")

@router.post("/Vibrations")
def create_vibration(vibration: Vibration):
    vibrations.append(vibration)
    return {"message": "Vibration created successfully."}