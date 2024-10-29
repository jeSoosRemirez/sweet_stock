"""Main settings."""

import os

from pydantic import computed_field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Class for settings."""

    debug: bool = os.environ.get("DEBUG", False)
    port: str = os.environ.get("PORT", "55055")

    db_host: str = os.environ.get("DB_HOST")
    db_port: str = os.environ.get("DB_PORT")
    db_user: str = os.environ.get("DB_USER")
    db_pass: str = os.environ.get("DB_PASS")
    db_name: str = os.environ.get("DB_NAME")

    @computed_field
    @property
    def psql_url(self) -> str:
        """Returns url for db with async driver."""
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}?async_fallback=True"
