from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base

class Chambre(Base):
    # [cite_start]Nom de la table dans la BDD [cite: 65]
    __tablename__ = "chambre" 

    # [cite_start]Colonnes correspondant au cahier des charges [cite: 66, 67, 68]
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    numero = Column(Integer, nullable=False)
    type = Column(Enum("simple", "double", "suite"))
    prix = Column(Integer, nullable=False)
    etat = Column(Enum("libre", "occupée", "réservée"))
    hotel_id = Column(Integer,ForeignKey('hotel.id'), nullable=False)
    hotel = relationship("Hotel")
    
    # Représentation de l'objet pour le débogage
    def __repr__(self):
        return f"<Hotel(id={self.id}, numéro='{self.numero}')>"