"""Services, to implement some logic we have"""
from typing import AsyncGenerator

from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService
from sqlalchemy.ext.asyncio import AsyncSession

from asyncpg import Connection

from crud.models import User
from crud.repos import UserRepository


class UserService(SQLAlchemyAsyncRepositoryService[User]):
    repository_type = UserRepository


async def provide_user_service(
    db_session: AsyncSession, ) -> AsyncGenerator[UserService, None]:
    """This provides the default Authors repository."""
    async with UserService.new(session=db_session) as service:
        yield service
