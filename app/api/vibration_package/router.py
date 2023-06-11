from fastapi import APIRouter, HTTPException
from .schemas import Vibration

router = APIRouter()

@router.get("/Vibrations/{device_id}", tags=["Vibrations"])
def get_vibrations_by_device_id(device_id: int):
    result = [vibration for vibration in vibrations if vibration.device_id == device_id]
    if result:
        return result
    raise HTTPException(status_code=404, detail="No vibrations found for the provided DeviceId.")

@router.get("/Vibrations/{device_id}/{date}", tags=["Vibrations"])
def get_vibrations_by_device_id_and_date(device_id: int, date: str):
    result = [vibration for vibration in vibrations if vibration.device_id == device_id and vibration.date == date]
    if result:
        return result
    raise HTTPException(status_code=404, detail="No vibrations found for the provided DeviceId and Date.")

@router.post("/Vibrations", tags=["Vibrations"])
def create_vibration(vibration: Vibration):
    vibrations.append(vibration)
    return {"message": "Vibration created successfully."}