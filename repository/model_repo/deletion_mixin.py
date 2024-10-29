"""Mixin for deletion in base model repo class."""

from functools import partial

from sqlalchemy import delete


class DeletionMethodMixin:
    """Mixin class for deletion methods in repo class."""

    async def delete_by_id(self, id_value, session_obj=None) -> bool:
        """Deletes obj by id and return if it was deleted."""
        deleted_count = await self.delete_by(
            self._model_klass.id == id_value,
            session_obj=session_obj,
        )
        return bool(deleted_count)

    async def delete_by(self, *filters, session_obj=None) -> int:
        """Deletes objs by filters and return deleted row amount."""
        performer = partial(self._delete_in_session, *filters)

        if session_obj:
            return await performer(session_obj=session_obj)

        async with self._session_maker() as _session:
            deleted_count = await performer(session_obj=_session)
            await _session.commit()

        return deleted_count

    async def _delete_in_session(self, *filters, session_obj) -> int:
        """Performs query for deleting objs by filters."""
        res = await session_obj.execute(delete(self._model_klass).where(*filters))
        return res.rowcount
