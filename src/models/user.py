
from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    role: str
    is_active: bool
    created_at: datetime


class Pagination(BaseModel):
    page: int
    page_size: int
    total: int
    total_pages: int


class UserListResponse(BaseModel):
    data: list[User]
    Pagination: Pagination
