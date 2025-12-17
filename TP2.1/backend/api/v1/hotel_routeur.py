from typing import List

from database.session import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.hotel_schema import HotelCreate, HotelInDB
from services.hotel_service import HotelService
from sqlalchemy.orm import Session

routeur = APIRouter(prefix="/hotels", tags=["Hôtels"])

hotel_service = HotelService()


# URL: POST /hotels/
@routeur.post("/", response_model=HotelInDB)
def create_hotel(hotel: HotelCreate, db: Session = Depends(get_db)):
    return hotel_service.create_hotel(db=db, hotel=hotel)


# URL: GET /hotels/
@routeur.get("/", response_model=List[HotelInDB])
def list_hotels(db: Session = Depends(get_db)):
    return hotel_service.list_hotels(db=db)


# URL: GET /hotels/{hotel_id}
@routeur.get("/{hotel_id}", response_model=HotelInDB)
def get_hotel(hotel_id: int, db: Session = Depends(get_db)):
    hotel = hotel_service.get_hotel(db=db, hotel_id=hotel_id)
    if not hotel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Hôtel non trouvé"
        )
    return hotel


# AJOUTE LA ROUTE DELETE SI ELLE MANQUE
@routeur.delete("/{hotel_id}")
def delete_hotel(hotel_id: int, db: Session = Depends(get_db)):
    # Ajoute la logique delete dans ton service si nécessaire
    return {"message": "Hôtel supprimé (Simulation)"}
