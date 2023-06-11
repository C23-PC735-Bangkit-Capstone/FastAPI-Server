from fastapi import APIRouter, HTTPException
from .schemas import Device

router = APIRouter()

devices = [
    {"id": 1, "device_id": 1, "pond_id": 1, "signal_strength": 80, "battery_strength": 80, "condition": "normal"},
    {"id": 2, "device_id": 2, "pond_id": 1, "signal_strength": 80, "battery_strength": 80, "condition": "normal"},
    {"id": 3, "device_id": 3, "pond_id": 2, "signal_strength": 80, "battery_strength": 80, "condition": "normal"},
]

@router.get("/Device", tags=["Device"])
def get_all_devices():
    if devices:
        return devices
    raise HTTPException(status_code=404, detail="No devices found.")

@router.get("/Device/{pond_id}", tags=["Device"])
def get_devices_by_pond_id(pond_id: int):
    result = [device for device in devices if device["pond_id"] == pond_id]
    if result:
        return result
    raise HTTPException(status_code=404, detail="No devices found for the provided PondId.")

@router.get("/Device/Device/{device_id}", tags=["Device"])
def get_device_by_id(device_id: int):
    for device in devices:
        if device["id"] == device_id:
            return device
    raise HTTPException(status_code=404, detail="Device not found.")

@router.put("/Device/{device_id}", tags=["Device"])
def update_device_by_id(device_id: int):
    for device in devices:
        if device["id"] == device_id:
            # Update the device information
            device["name"] = "Updated Device"
            return {"message": "Device updated successfully."}
    raise HTTPException(status_code=404, detail="Device not found.")

@router.delete("/Device/{device_id}", tags=["Device"])
def delete_device_by_id(device_id: int):
    for i, device in enumerate(devices):
        if device["id"] == device_id:
            del devices[i]
            return {"message": "Device deleted successfully."}
    raise HTTPException(status_code=404, detail="Device not found.")

@router.post("/Device", tags=["Device"])
def create_device(device: Device):
    devices.append(device)
    return {"message": "Device created successfully."}
