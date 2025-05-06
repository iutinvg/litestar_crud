"""Create connection"""
from litestar_asyncpg import AsyncpgConfig, AsyncpgPlugin, PoolConfig
from litestar.plugins.sqlalchemy import AsyncSessionConfig, SQLAlchemyAsyncConfig
from litestar.plugins.sqlalchemy import SQLAlchemyPlugin

from crud.conf import Conf


def get_asyncpg_plugin() -> AsyncpgPlugin:
    """Plugin configued wuth connection"""
    name = Conf.db.name
    user = Conf.db.user
    password = Conf.db.password
    creds = f"postgresql://{user}:{password}@localhost/{name}"
    pool = PoolConfig(dsn=creds)
    asyncpg = AsyncpgPlugin(config=AsyncpgConfig(pool_config=pool))
    return asyncpg


def get_alchemy_plugin() -> SQLAlchemyPlugin:
    name = Conf.db.name
    user = Conf.db.user
    password = Conf.db.password
    creds = f"postgresql+asyncpg://{user}:{password}@localhost/{name}"
    session_config = AsyncSessionConfig(expire_on_commit=False)
    sqlalchemy_config = SQLAlchemyAsyncConfig(
        connection_string=
        "postgresql+asyncpg://postgres:359f94cc28ee@localhost/crud_db",
        before_send_handler="autocommit",
        session_config=session_config,
        create_all=True,
    )
    alchemy = SQLAlchemyPlugin(config=sqlalchemy_config)
    return alchemy
