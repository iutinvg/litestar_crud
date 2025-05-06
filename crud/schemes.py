"""
Schemes is used to avoid confusion with db models.
Schemes is to work data on service level.
"""
from typing import Annotated
from datetime import datetime

from msgspec import Struct, Meta


class UserBase(Struct):
    """Minimal info set"""
    name: str
    surname: str


class UserGet(UserBase):
    """Plus some internal info"""
    id: int
    password: str
    created_at: datetime


class UserCreate(UserBase):
    """Get + password"""
    password: Annotated[str, Meta(min_length=6)]
    password1: str

    def __post_init__(self):
        if self.password != self.password1:
            raise ValueError("Passwords don't match")


class UserUpdate(UserCreate):
    """Maybe (100%) will be differnt in the future"""
