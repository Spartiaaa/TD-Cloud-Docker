# api/v1/hotel_router.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.session import get_db
from schemas.hotel_schema import HotelCreate, HotelInDB
from services.hotel_service import HotelService

# Un seul router
routeur = APIRouter(
    prefix="/hotels",
    tags=["Hôtels"]
)

# Instanciation du Service
hotel_service = HotelService()

@routeur.post("/create", response_model=HotelInDB)  # "/" car le prefix est déjà "/hotels"
def create_hotel(hotel: HotelCreate, db: Session = Depends(get_db)):
    # Logique pour créer l'hôtel via le service
    new_hotel = hotel_service.create_hotel(db=db, hotel=hotel)
    return new_hotel

@routeur.get("/list", response_model=List[HotelInDB])
def list_hotels(db: Session = Depends(get_db)):
    return hotel_service.list_hotels(db=db)

@routeur.get("/get/{hotel_id}", response_model=HotelInDB)
def get_hotel(hotel_id: int, db: Session = Depends(get_db)):
    hotel = hotel_service.get_hotel(db=db, hotel_id=hotel_id)
    if not hotel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Hôtel non trouvé")
    return hotel

