"""Database session maker."""

from sqlalchemy import Engine, create_engine
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import Session, sessionmaker


def make_db(
    db_url: str,
    *,
    is_async: bool = True,
) -> tuple[
    AsyncEngine | Engine,
    async_sessionmaker[AsyncSession] | sessionmaker[Session],
]:
    """Creates engine and session.

    Args:
        db_url (str): URL for database
        is_debug (bool): used for enabling echo in sqlalchemy engine
        is_async (bool): used to choose async or sync engine and session

    Returns:
        tuple: tuple with engine and session
            - First element is AsyncEngine or Engine
            - Second element is AsyncSession or Session
    """
    engine_create_func = create_async_engine if is_async else create_engine
    engine = engine_create_func(db_url, future=True, pool_pre_ping=True)

    sessionmaker_func = async_sessionmaker if is_async else sessionmaker
    async_session = sessionmaker_func(
        autocommit=False,
        autoflush=False,
        expire_on_commit=False,
        bind=engine,
    )

    return engine, async_session
