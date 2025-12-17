# schemas/hotel_schema.py
from pydantic import BaseModel
from typing import Optional

class HotelBase(BaseModel):
    nom: str
    adresse: str

class HotelCreate(HotelBase):
    pass  # héritage pour création

class HotelInDB(HotelBase):
    id: int
    model_config = {
        "from_attributes": True
    }




