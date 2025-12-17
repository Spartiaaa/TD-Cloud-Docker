from sqlalchemy.orm import Session
from models import Reservation, Chambre, Client
from schemas.reservation_schema import ReservationCreate, ReservationInDB


class ReservationService:
    def create_reservation(self, db: Session, reservation: ReservationCreate) -> ReservationInDB:
        new_reservation = Reservation(
            date_debut= reservation.date_debut,
            date_fin= reservation.date_fin,
            status= reservation.status,
            client_id= reservation.client_id,
            chambre_id= reservation.chambre_id
        )

        db.add(new_reservation)
        db.commit()
        db.refresh(new_reservation)
        return new_reservation
    
    def list_reservations(self, db: Session):
        return db.query(Reservation).all()
    
    def delete_reservation(self, db: Session, reservation_id: int) -> bool:
        reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()
        if not reservation:
            return False
        db.delete(reservation)
        db.commit()
        return True