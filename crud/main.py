"""All entry points"""
from litestar import Litestar
from litestar.params import Parameter
from litestar.di import Provide
from litestar.repository.filters import LimitOffset, FilterTypes

from crud.db import get_asyncpg_plugin, get_alchemy_plugin
from crud.controllers import UserController, HealthCheckController
from crud.conf import Conf


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


asyncpg = get_asyncpg_plugin()
alchemy = get_alchemy_plugin()

app = Litestar(
    debug=Conf.debug,
    route_handlers=[UserController, HealthCheckController],
    plugins=[alchemy, asyncpg],
    dependencies={
        "limit_offset":
        Provide(provide_limit_offset_pagination, sync_to_thread=False)
    },
)
