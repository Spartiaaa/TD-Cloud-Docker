from typing import Optional

from pydantic import BaseModel


class ClientBase(BaseModel):
    nom: str
    email: str
    tel: str


class ClientCreate(ClientBase):
    pass

class ClientInDB(ClientBase):
    id: int
    model_config = {"from_attributes": True}
