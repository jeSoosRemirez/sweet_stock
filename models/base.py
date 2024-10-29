"""Module with base model class and engine, session objects."""

from functools import partial

from database.builder import make_db
from repository.model_repo.model_repo import ModelRepo as _ModelRepo
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase

from config import settings


class BaseModel(AsyncAttrs, DeclarativeBase):
    """Base class for models."""


engine, AsyncSession = make_db(settings.psql_url)

ModelRepo = partial(_ModelRepo, engine, AsyncSession)
