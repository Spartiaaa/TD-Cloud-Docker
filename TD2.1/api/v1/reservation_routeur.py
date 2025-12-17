from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.session import get_db
from schemas.reservation_schema import ReservationCreate, ReservationInDB
from services.reservation_service import ReservationService

# Un seul router
routeur = APIRouter(
    prefix="/reservations",
    tags=["Reservations"]
)

@routeur.post("/create", response_model=ReservationInDB)  # "/" car le prefix est déjà "/reservations"
def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    reservation_service = ReservationService()
    new_reservation = reservation_service.create_reservation(db=db, reservation=reservation)
    return new_reservation

@routeur.get("/list", response_model=List[ReservationInDB])
def list_reservations(db: Session = Depends(get_db)):
    reservation_service = ReservationService()
    return reservation_service.list_reservations(db=db)

@routeur.delete("/delete/{reservation_id}")
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)): 
    reservation_service = ReservationService()
    success = reservation_service.delete_reservation(db=db, reservation_id=reservation_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Réservation non trouvée")
    return {"detail": "Réservation supprimée avec succès"}



