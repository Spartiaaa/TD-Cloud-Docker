from typing import List

from database.session import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.client_schema import ClientCreate, ClientInDB
from services.client_service import ClientService
from sqlalchemy.orm import Session

routeur = APIRouter(prefix="/clients", tags=["Clients"])

client_service = ClientService()  # Correction du nom de variable


# URL: POST /clients/
@routeur.post("/", response_model=ClientInDB)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    return client_service.create_client(db=db, client=client)


# URL: GET /clients/{client_id}
@routeur.get("/{client_id}", response_model=ClientInDB)
def detail_client(client_id: int, db: Session = Depends(get_db)):
    client = client_service.detail_client(db=db, client_id=client_id)
    if not client:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Client non trouvé"
        )
    return client


@routeur.get("/", response_model=List[ClientInDB])
def list_clients(db: Session = Depends(get_db)):
    # Assure-toi d'avoir une méthode list_clients dans ton service !
    return client_service.list_clients(db=db)
