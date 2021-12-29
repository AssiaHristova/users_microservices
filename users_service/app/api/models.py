from typing import Optional, List

from pydantic import BaseModel, Field

from addresses_service.app.api.models import AddressIn, AddressCls


class UserDTOCls:
    def __init__(self, *, id: int, first_name: str = None, last_name: str = None, addresses: List[AddressCls]):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = addresses


class UserIn(BaseModel):
    id: int
    first_name: str
    last_name: str


class UserOut(UserIn):
    id: int


class UserUpdate(UserIn):
    first_name: str
    last_name: str


class UserDTO(BaseModel):
    id: int
    first_name: str
    last_name: str
    addresses: List[AddressIn]

 #   class Config:
  #      orm_mode = True
