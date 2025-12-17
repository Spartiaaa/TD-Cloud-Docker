# api/v1/hotel_router.py
from typing import List

from database.session import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.chambre_schema import ChambreCreate, ChambreInDB, ChambreUpdate
from services.chambre_service import ChambreService
from sqlalchemy.orm import Session

# Un seul router
routeur = APIRouter(prefix="/chambres", tags=["Chambres"])
chambre_service = ChambreService()


@routeur.post("/", response_model=ChambreInDB)  # "/" car le prefix est déjà "/chambres"
def create_chambre(chambre: ChambreCreate, db: Session = Depends(get_db)):
    new_chambre = chambre_service.create_chambre(db=db, chambre=chambre)
    return new_chambre


@routeur.get("/{hotel_id}", response_model=List[ChambreInDB])
def list_rooms_by_hotel(hotel_id: int, db: Session = Depends(get_db)):
    return chambre_service.list_rooms_by_hotel(db=db, hotel_id=hotel_id)


@routeur.put("/{chambre_id}")
def update_chambre(
    chambre_id: int, chambre_update: ChambreUpdate, db: Session = Depends(get_db)
):
    updated_chambre = chambre_service.update_chambre(db, chambre_id, chambre_update)
    if not updated_chambre:
        raise HTTPException(status_code=404, detail="Chambre non trouvée")
    return updated_chambre


@routeur.get("/{chambre_id}")
def get_etat_chambre(chambre_id: int, db: Session = Depends(get_db)):
    etat = chambre_service.get_etat_chambre(db, chambre_id)
    if etat is None:
        raise HTTPException(status_code=404, detail="Chambre non trouvée")
    return {"etat": etat}
