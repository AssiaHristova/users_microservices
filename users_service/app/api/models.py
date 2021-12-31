from typing import Optional, List

from pydantic import BaseModel, Field

from addresses_service.app.api.models import AddressIn


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

