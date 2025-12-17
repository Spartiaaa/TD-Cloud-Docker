from sqlalchemy.orm import Session
from models import Hotel
from schemas.hotel_schema import HotelCreate, HotelInDB

class HotelService:
    def create_hotel(self, db: Session, hotel: HotelCreate) -> HotelInDB:
        new_hotel = Hotel(
            nom=hotel.nom,
            adresse=hotel.adresse,
        )
        db.add(new_hotel)
        db.commit()
        db.refresh(new_hotel)
        return new_hotel

    def list_hotels(self, db: Session):
        return db.query(Hotel).all()
    
    def get_hotel(self, db: Session, hotel_id: int) -> HotelInDB:
        return db.query(Hotel).filter(Hotel.id == hotel_id).first()
    
    def delete_hotel(self, db: Session, hotel_id: int) -> bool:
        hotel = db.query(Hotel).filter(Hotel.id == hotel_id).first()
        if hotel:
            db.delete(hotel)
            db.commit()
            return True
        return False

    
