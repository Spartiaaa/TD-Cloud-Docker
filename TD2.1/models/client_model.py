from sqlalchemy import Column, Integer, String
from database.base import Base

class Client(Base):
    # [cite_start]Nom de la table dans la BDD [cite: 65]
    __tablename__ = "client" 

    # [cite_start]Colonnes correspondant au cahier des charges [cite: 66, 67, 68]
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nom = Column(String(255), nullable=False)
    email = Column(String(255), nullable=True)
    tel = Column(String(20), nullable=False)
