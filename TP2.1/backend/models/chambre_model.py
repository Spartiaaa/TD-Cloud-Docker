from database.base import Base
from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Chambre(Base):
    __tablename__ = "chambre"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    numero = Column(Integer, nullable=False)
    type = Column(Enum("simple", "double", "suite"))
    prix = Column(Integer, nullable=False)
    etat = Column(Enum("libre", "occupee", "maintenance"))
    hotel_id = Column(Integer, ForeignKey("hotel.id"), nullable=False)
    hotel = relationship("Hotel")

    def __repr__(self):
        return f"<Hotel(id={self.id}, numéro='{self.numero}')>"
