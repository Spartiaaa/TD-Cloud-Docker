from sqlalchemy import Column, Integer, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database.base import Base
# Définition pour une table 'réservation'

class Reservation(Base): # ou Model, selon votre configuration
    
    __tablename__ = "reservation"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date_debut = Column(Date, nullable=False)
    date_fin = Column(Date, nullable=False)
    status = Column(Enum("confirmee", "annulee"), nullable=False, default="confirmee")
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    chambre_id = Column(Integer, ForeignKey('chambre.id'), nullable=False)