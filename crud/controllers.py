"""Services"""
from litestar import Controller, get, post, patch, delete
from litestar.di import Provide
from litestar.pagination import OffsetPagination
from litestar.repository.filters import LimitOffset

from asyncpg import Connection

from crud.services import provide_user_service, UserService
from crud.schemes import UserGet, UserCreate, UserUpdate
from crud.models import User


class HealthCheckController(Controller):
    """
    Controller with direct connection from a pool
    Maybe can be useful to check DB health.
    """

    @get(path="/health_check")
    async def health_check(self, db_connection: Connection) -> dict[str, str]:
        """Check database available and returns app config info."""
        result = await db_connection.fetch("select 1")
        return {"select_1": str(result)}


class UserController(Controller):
    """Users"""
    path = "/users"
    dependencies = {"user_service": Provide(provide_user_service)}

    @get()
    async def list_users(
            self, user_service: UserService,
            limit_offset: LimitOffset) -> OffsetPagination[UserGet]:
        """List"""
        results, total = await user_service.list_and_count(limit_offset)
        return user_service.to_schema(
            data=results,
            total=total,
            filters=[limit_offset],
            schema_type=UserGet,
        )

    @post()
    async def create_user(
        self,
        user_service: UserService,
        data: UserCreate,
    ) -> UserGet:
        """New user"""
        obj = await user_service.create(data)
        return user_service.to_schema(data=obj, schema_type=UserGet)

    @get(path="/{user_id:int}")
    async def get_user(
        self,
        user_service: UserService,
        user_id: int,
    ) -> UserGet:
        """Get existing"""
        obj = await user_service.get(user_id)
        return user_service.to_schema(data=obj, schema_type=UserGet)

    @get(path="/check_password/{user_id:int}")
    async def check_password(self, user_service: UserService, user_id: int,
                             password: str) -> dict:
        """"""
        obj: User = await user_service.get(user_id)
        return {'ok': obj.password.verify(password)}

    @patch(path="/{user_id:int}")
    async def update_user(
        self,
        user_service: UserService,
        data: UserUpdate,
        user_id: int,
    ) -> UserGet:
        """Change"""
        obj = await user_service.update(data=data, item_id=user_id)
        return user_service.to_schema(obj, schema_type=UserGet)

    @delete(path="/{user_id:int}")
    async def delete_user(
        self,
        user_service: UserService,
        user_id: int,
    ) -> None:
        """Remove"""
        await user_service.delete(user_id)
