from sqlalchemy import Column, Integer, String
from database.base import Base

class Client(Base):
    
    __tablename__ = "client" 

   
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nom = Column(String(255), nullable=False)
    email = Column(String(255), nullable=True)
    tel = Column(String(20), nullable=False)
