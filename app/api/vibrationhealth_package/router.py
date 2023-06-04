from fastapi import APIRouter
from .models import VibrationHealth
from datetime import datetime

router = APIRouter()

vibration_health_data = [
    VibrationHealth(id=1, timestamp=datetime(2023, 1, 1, 23, 3, 20), device_id=1, health_category="Good", health_score=80),
    VibrationHealth(id=1, timestamp=datetime(2023, 1, 1, 23, 3, 20), device_id=1, health_category="Fair", health_score=50),
    VibrationHealth(id=1, timestamp=datetime(2023, 1, 1, 23, 3, 20), device_id=2, health_category="Excellent", health_score=100),
]

@router.get("/VibrationHealth/{device_id}")
def get_vibration_health_by_device_id(device_id: int):
    result = [health for health in vibration_health_data if health.device_id == device_id]
    if result:
        return result
    raise HTTPException(status_code=404, detail="No vibration health data found for the provided DeviceId.")

@router.get("/VibrationHealth/{device_id}/{date}")
def get_vibration_health_by_device_id_and_date(device_id: int, date: str):
    result = [health for health in vibration_health_data if health.device_id == device_id and health.date == date]
    if result:
        return result
    raise HTTPException(status_code=404, detail="No vibration health data found for the provided DeviceId and Date.")

@router.post("/VibrationHealth")
def create_vibration_health(vibration_health: VibrationHealth):
    vibration_health_data.append(vibration_health)
    return {"message": "Vibration health data created successfully."}
