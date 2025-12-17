# models/hotel_model.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.base import Base

class Hotel(Base):
    
    __tablename__ = "hotel" 

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nom = Column(String(255), nullable=False)
    adresse = Column(String(255), nullable=True) 
    
    def __repr__(self):
        return f"<Hotel(id={self.id}, nom='{self.nom}')>"
