"""Mixin for model repo with creation methods."""

from functools import partial


class CreationMethodMixin:
    """Mixin class for model repo class with creation methods."""

    async def create_one(self, creation_data, session_obj=None):
        """Creates objects and return it."""
        return (await self.create_many(creation_data, session_obj=session_obj))[0]

    async def create_many(self, *creation_datas: dict, session_obj=None) -> tuple:
        """Creates objects and returns it."""
        performer = partial(self._add_to_session, *creation_datas)

        if session_obj:
            return performer(session_obj=session_obj)

        async with self._session_maker() as _session:
            objs = performer(session_obj=_session)
            await _session.commit()
            for obj in objs:
                await _session.refresh(obj)

        return objs

    def _add_to_session(self, *creation_datas: dict, session_obj):
        """Adds objects to session."""
        objects_to_create = tuple(
            self._model_klass(**creation_data) for creation_data in creation_datas
        )
        session_obj.add_all(objects_to_create)
        return objects_to_create
