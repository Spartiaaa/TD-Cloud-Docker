from sqlalchemy.orm import Session
from models import Chambre
from schemas.chambre_schema import ChambreCreate, ChambreInDB, ChambreUpdate

class ChambreService:
    def create_chambre(self, db: Session, chambre: ChambreCreate) -> ChambreInDB:
        new_chambre = Chambre(
            numero=chambre.numero,
            type=chambre.type,
            prix=chambre.prix,
            etat=chambre.etat,
            hotel_id=chambre.hotel_id,
        )
        db.add(new_chambre)
        db.commit()
        db.refresh(new_chambre)
        return new_chambre

    def list_rooms_by_hotel(self, db: Session, hotel_id: int):
            return (
                db.query(Chambre).filter(Chambre.hotel_id == hotel_id).all()
            )
    
    def update_chambre(self, db: Session, chambre_id: int, chambre_data: ChambreUpdate) -> ChambreInDB | None:
        chambre = db.query(Chambre).filter(Chambre.id == chambre_id).first()
        if not chambre:
            return None        
        # Sinon, votre boucle actuelle est parfaite :
        for key, value in chambre_data.model_dump(exclude_unset=True).items():
            setattr(chambre, key, value)    
        db.commit()
        db.refresh(chambre)
        
        return chambre
    
    def get_etat_chambre(self, db: Session, chambre_id: int) -> str | None:
        chambre = db.query(Chambre).filter(Chambre.id == chambre_id).first()
        if chambre:
            return chambre.etat
        return None
