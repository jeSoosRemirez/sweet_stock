"""Mixin for base repo for retrieving objs."""

from functools import partial

from sqlalchemy import select
from sqlalchemy.orm import joinedload, subqueryload


class RetrivingMethodMixin:
    """Mixin class for base repo with retrieving methods."""

    async def retrieve_by_id(
        self,
        id_value,
        joinedloads: list | tuple | None = None,
        subqueryloads: list | tuple | None = None,
        session_obj=None,
    ):
        """Returns obj by id or None."""
        objs = await self.retrieve(
            self._model_klass.id == id_value,
            session_obj=session_obj,
            joinedloads=joinedloads,
            subqueryloads=subqueryloads,
        )

        assert len(objs) < 2
        return objs[0] if objs else None

    async def retrieve(
        self,
        *filters,
        session_obj=None,
        offset: int | None = None,
        limit: int | None = None,
        order_by: list | tuple | None = None,
        joinedloads: list | tuple | None = None,
        subqueryloads: list | tuple | None = None,
    ) -> list:
        """Returns objects."""
        performer = partial(
            self._perform_retrive,
            *filters,
            offset=offset,
            limit=limit,
            order_by=order_by,
            joinedloads=joinedloads,
            subqueryloads=subqueryloads,
        )

        if session_obj:
            return await performer(session_obj=session_obj)

        async with self._session_maker() as _session:
            return await performer(
                session_obj=_session,
            )

    async def _perform_retrive(
        self,
        *filters,
        session_obj,
        offset: int | None = None,
        limit: int | None = None,
        order_by: list | tuple | None = None,
        joinedloads: list | tuple | None = None,
        subqueryloads: list | tuple | None = None,
    ) -> list:
        """Performs retrieve query."""
        query = select(self._model_klass)

        if filters:
            query = query.where(*filters)

        if offset is not None:
            query = query.offset(offset)

        if limit is not None:
            query = query.limit(limit)

        if order_by:
            query = query.order_by(*order_by)

        if joinedloads:
            query = query.options(
                *tuple(joinedload(relation) for relation in joinedloads),
            )

        if subqueryloads:
            query = query.options(
                *tuple(subqueryload(relation) for relation in subqueryloads),
            )

        result = await session_obj.execute(query)

        return result.scalars().all()
