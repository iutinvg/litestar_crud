"""Create connection"""
from litestar_asyncpg import AsyncpgConfig, AsyncpgPlugin, PoolConfig

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
