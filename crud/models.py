"""
DB models to use in DTO.
"""
from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy.orm import Mapped, mapped_column

from crud.hashed_password import NativeHasher, PasswordHash
from crud.conf import Conf

# id BIGINT PRIMARY KEY, автоинкремент
# name
# surname
# password
# created_at TIMESTAMP UTC-0
# updated_at TIMESTAMP UTC-0


class User(BigIntAuditBase):
    """User model"""
    __tablename__ = 'crud_users'
    name: Mapped[str]
    surname: Mapped[str]
    password: Mapped[str] = mapped_column(
        PasswordHash(backend=NativeHasher(salt=Conf.salt)))
