"""Mixin for updating methods for model repo class."""

from functools import partial

from sqlalchemy import update
from sqlalchemy.orm import joinedload


class UpdatingMethodMixin:
    """Mixin class for model repo with updating methods."""

    async def update_by_id(
        self,
        id_value,
        load_relations: tuple | list | None = None,
        session_obj=None,
        **values,
    ):
        """Update obj by id and return it."""
        updated_objs = await self.update(
            self._model_klass.id == id_value,
            load_relations=load_relations,
            session_obj=session_obj,
            **values,
        )

        assert len(updated_objs) < 2

        return updated_objs[0] if updated_objs else None

    async def update(
        self,
        *filters,
        session_obj=None,
        load_relations: tuple | list | None = None,
        **values,
    ) -> list:
        """Updates objs by filters and returns it."""
        performer = partial(
            self._perform_update,
            *filters,
            load_relations=load_relations,
            **values,
        )

        if session_obj:
            return await performer(session_obj=session_obj)

        async with self._session_maker() as _session:
            updated_obj = await performer(session_obj=_session)
            await _session.commit()

        return updated_obj

    async def _perform_update(
        self,
        *filters,
        session_obj,
        load_relations: tuple | list | None = None,
        **values,
    ) -> list:
        """Performs obj updating."""
        query = (
            update(self._model_klass)
            .where(*filters)
            .values(**values)
            .returning(self._model_klass)
        )

        if load_relations:
            query = query.options(
                *tuple(joinedload(relation) for relation in load_relations),
            )
        result = await session_obj.execute(query)

        return result.scalars().all()
