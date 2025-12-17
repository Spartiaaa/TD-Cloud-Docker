# models/hotel_model.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.base import Base

class Hotel(Base):
    # [cite_start]Nom de la table dans la BDD [cite: 65]
    __tablename__ = "hotel" 

    # [cite_start]Colonnes correspondant au cahier des charges [cite: 66, 67, 68]
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nom = Column(String(255), nullable=False)
    adresse = Column(String(255), nullable=True) # Utilisation de String(255) à la place de TEXT simple
    
    # Représentation de l'objet pour le débogage
    def __repr__(self):
        return f"<Hotel(id={self.id}, nom='{self.nom}')>"