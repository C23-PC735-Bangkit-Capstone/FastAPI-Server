from fastapi import APIRouter, HTTPException
from .models import Pond

router = APIRouter()

ponds = [
    Pond(id=1, pond_id=1, user_id=1, pond_location="37.700421688980136, -81.84535319999998"),
    Pond(id=2, pond_id=2, user_id=1, pond_location="37.700421688980136, -81.84535319999998"),
    Pond(id=3, pond_id=3, user_id=2, pond_location="37.700421688980136, -81.84535319999998"),
]

@router.get("/Ponds")
def get_all_ponds():
    if ponds:
        return ponds
    raise HTTPException(status_code=404, detail="No ponds found.")

@router.get("/Ponds/{user_id}")
def get_ponds_by_user_id(user_id: int):
    result = [pond for pond in ponds if pond.user_id == user_id]
    if result:
        return result
    raise HTTPException(status_code=404, detail="No ponds found for the provided UserId.")

@router.get("/Ponds/Pond/{pond_id}")
def get_pond_by_id(pond_id: int):
    for pond in ponds:
        if pond.id == pond_id:
            return pond
    raise HTTPException(status_code=404, detail="Pond not found.")

@router.put("/Ponds/{pond_id}")
def update_pond_by_id(pond_id: int, pond: Pond):
    for p in ponds:
        if p.id == pond_id:
            # Update the pond information
            p.name = pond.name
            return {"message": "Pond updated successfully."}
    raise HTTPException(status_code=404, detail="Pond not found.")

@router.delete("/Ponds/{pond_id}")
def delete_pond_by_id(pond_id: int):
    for i, pond in enumerate(ponds):
        if pond.id == pond_id:
            del ponds[i]
            return {"message": "Pond deleted successfully."}
    raise HTTPException(status_code=404, detail="Pond not found.")

@router.post("/Ponds")
def create_pond(pond: Pond):
    ponds.append(pond)
    return {"message": "Pond created successfully."}