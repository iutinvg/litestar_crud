"""All entry points"""
from litestar import Litestar
from litestar.plugins.sqlalchemy import AsyncSessionConfig, SQLAlchemyAsyncConfig
from litestar.plugins.sqlalchemy import SQLAlchemyPlugin
from litestar.params import Parameter
from litestar.di import Provide
from litestar.repository.filters import LimitOffset, FilterTypes

from crud.db import get_asyncpg_plugin
from crud.controllers import UserController, UserC

# asyncpg = get_asyncpg_plugin()
# app = Litestar(plugins=[asyncpg], route_handlers=[UserController])

session_config = AsyncSessionConfig(expire_on_commit=False)
sqlalchemy_config = SQLAlchemyAsyncConfig(
    connection_string=
    "postgresql+asyncpg://postgres:359f94cc28ee@localhost/crud_db",
    before_send_handler="autocommit",
    session_config=session_config,
    create_all=True,
)
alchemy = SQLAlchemyPlugin(config=sqlalchemy_config)


def provide_limit_offset_pagination(
    current_page: int = Parameter(ge=1,
                                  query="currentPage",
                                  default=1,
                                  required=False),
    page_size: int = Parameter(
        query="pageSize",
        ge=1,
        default=10,
        required=False,
    ),
) -> FilterTypes:
    """Add offset/limit pagination."""
    return LimitOffset(page_size, page_size * (current_page - 1))


app = Litestar(
    route_handlers=[UserC],
    plugins=[alchemy],
    dependencies={
        "limit_offset":
        Provide(provide_limit_offset_pagination, sync_to_thread=False)
    },
)
