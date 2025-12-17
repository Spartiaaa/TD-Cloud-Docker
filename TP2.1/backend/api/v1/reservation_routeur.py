from typing import List

from database.session import get_db
from fastapi import APIRouter, Depends
from schemas.reservation_schema import ReservationCreate, ReservationInDB
from services.reservation_service import ReservationService
from sqlalchemy.orm import Session

# Un seul router
routeur = APIRouter(prefix="/reservations", tags=["Reservations"])

reservation_service = ReservationService()


# 1. CRÉATION
@routeur.post("/", response_model=ReservationInDB)
def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    reservation_service = ReservationService()
    # Pas de changement ici
    return reservation_service.create_reservation(db=db, reservation=reservation)


# 2. LISTE
@routeur.get("/", response_model=List[ReservationInDB])
def list_reservations(db: Session = Depends(get_db)):
    reservation_service = ReservationService()
    return reservation_service.list_reservations(db=db)


# 3. SUPPRESSION
@routeur.delete("/{reservation_id}")
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    reservation_service = ReservationService()
    # Ajoute ici la logique de retour comme on a vu avant
    return reservation_service.delete_reservation(db=db, reservation_id=reservation_id)
