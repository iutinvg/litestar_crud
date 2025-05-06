"""Reposity: a layer to deal with DB directly"""
from advanced_alchemy.repository import SQLAlchemyAsyncRepository

from crud.models import User


class UserRepository(SQLAlchemyAsyncRepository[User]):
    model_type = User
