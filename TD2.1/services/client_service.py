from sqlalchemy.orm import Session
from models import Client
from schemas.client_schema import ClientCreate, ClientInDB

class ClientService:
    def create_client(self, db: Session, client: ClientCreate) -> ClientInDB:
        new_client = Client(
            nom=client.nom,
            email=client.email,
            tel=client.tel,
        )
        db.add(new_client)
        db.commit()
        db.refresh(new_client)
        return new_client
    
    def detail_client(self, db: Session, client_id: int) -> ClientInDB | None:
        return db.query(Client).filter(Client.id == client_id).first()