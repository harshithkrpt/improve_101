from pydantic import BaseModel
from typing import List

class ListDaoIn(BaseModel):
    title: str
    description: str
    owner_id: int


class ListAPIRequest(BaseModel):
    title: str
    description: str
    is_public: bool
    owner_id: int | None = None

class UpdateListIn(BaseModel):
    title: str | None = None
    description: str | None = None
    is_public: bool | None = None
    id: int | None = None


class BookMarkListIn(BaseModel):
    url: str
    title: str
    notes: str
    tags: List[str]
    read: bool
