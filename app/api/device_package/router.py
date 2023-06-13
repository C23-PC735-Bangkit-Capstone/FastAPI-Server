from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .schemas import Device as DeviceSchema
from app.models import Device as DeviceModel
from app.database import get_db

router = APIRouter()

@router.get("/device", response_model=List[DeviceSchema], tags=["Device"])
def get_all_devices(db: Session = Depends(get_db)):
    devices = db.query(DeviceModel).all()
    if not devices:
        raise HTTPException(status_code=404, detail="Device data not found")
    return devices

@router.post("/device", response_model=List[DeviceSchema], tags=["Device"])
def create_device(device: DeviceSchema, db: Session = Depends(get_db)):
    db_device = DeviceModel(**device.dict())
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return [device]

@router.get("/device/{pond_id}", response_model=List[DeviceSchema], tags=["Device"])
def get_devices_by_pond_id(pond_id: int, db: Session = Depends(get_db)):
    devices = db.query(DeviceModel).filter(DeviceModel.pond_id == pond_id).all()
    if not devices:
        raise HTTPException(status_code=404, detail="Device data not found for the user ID")
    return devices


@router.get("/device/Device/{device_id}", response_model=List[DeviceSchema], tags=["Device"])
def get_device_by_device_id(device_id: int, db: Session = Depends(get_db)):
    devices = db.query(DeviceModel).filter(DeviceModel.device_id == device_id).all()
    if not devices:
        raise HTTPException(status_code=404, detail="Device data not found for the user ID")
    return devices


@router.put("/device/{device_id}", response_model=DeviceSchema, tags=["Device"])
def update_device_by_id(device_id: int, updated_device: DeviceSchema, db: Session = Depends(get_db)):
    device = db.query(DeviceModel).filter(DeviceModel.device_id == device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Device data not found for the pond ID")
    for attr, value in updated_device.dict(exclude_unset=True).items():
        setattr(device, attr, value)
    db.commit()
    db.refresh(device)
    return device

@router.delete("/device/{device_id}", response_model=DeviceSchema, tags=["Device"])
def delete_device_by_id(device_id: int, db: Session = Depends(get_db)):
    device = db.query(DeviceModel).filter(DeviceModel.device_id == device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Device not found.")
    db.delete(device)
    db.commit()
    return device
