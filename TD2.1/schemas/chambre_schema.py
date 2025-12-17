from pydantic import BaseModel
from typing import Optional

class ChambreBase(BaseModel):
    numero: int
    type: str
    prix : float
    etat : str
    hotel_id : int

class ChambreCreate(ChambreBase):
    pass

class ChambreInDB(ChambreBase):
    id : int
    model_config = {
        "from_attributes": True
    }

class ChambreUpdate(BaseModel):
    numero: Optional[int] = None 
    type: Optional[str] = None
    prix : Optional[float] = None
    etat : Optional[str] = None
    hotel_id: Optional[int] = None

