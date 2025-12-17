from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.session import get_db
from schemas.client_schema import ClientCreate, ClientInDB
from services.client_service import ClientService

routeur = APIRouter(
    prefix="/clients",
    tags=["Clients"]
)

chambre_service = ClientService()
@routeur.post("/create", response_model=ClientInDB)  # "/" car le prefix est déjà "/clients"
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    new_client = chambre_service.create_client(db=db, client=client)
    return new_client

@routeur.get("/get/{client_id}", response_model=ClientInDB)
def detail_client(client_id: int, db: Session = Depends(get_db)):
    client = chambre_service.detail_client(db=db, client_id=client_id)
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Client non trouvé")
    return client
