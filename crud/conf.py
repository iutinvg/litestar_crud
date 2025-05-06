"""Project settings: DB credentials, common flags, etc"""
from dataclasses import dataclass, field
import os
from dotenv import load_dotenv

load_dotenv('dev.env')


@dataclass
class DBConf:
    name: str = os.getenv('POSTGRES_DB')
    user: str = os.getenv('POSTGRES_USER')
    password: str = os.getenv('POSTGRES_PASSWORD')


@dataclass
class Conf:
    """Basic app settings"""
    debug: bool = True
    db: DBConf = field(default=DBConf)
