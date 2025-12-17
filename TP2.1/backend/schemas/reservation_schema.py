from pydantic import BaseModel
from typing import Optional
from datetime import date

class ReservationBase(BaseModel):
    date_debut: date
    date_fin: date
    status: Optional[str] = "confirmee"
    client_id: int
    chambre_id: int

class ReservationCreate(ReservationBase):
    pass

class ReservationInDB(ReservationBase):
    id: int
    model_config = {
        "from_attributes": True
    }