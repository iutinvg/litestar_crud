"""
DB models to use in DTO.
"""
from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy.orm import DeclarativeBase, Mapped

# id BIGINT PRIMARY KEY, автоинкремент
# name
# surname
# password
# created_at TIMESTAMP UTC-0
# updated_at TIMESTAMP UTC-0

# class Base(DeclarativeBase):
#     """For now it's used in alembic"""
#     pass


class User(BigIntAuditBase):
    """User model"""
    name: Mapped[str]
    surname: Mapped[str]
    password: Mapped[str]
