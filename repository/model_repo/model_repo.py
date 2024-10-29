"""Repository for sa models."""

from .creation_mixin import CreationMethodMixin
from .deletion_mixin import DeletionMethodMixin
from .retrieving_mixin import RetrivingMethodMixin
from .updating_mixin import UpdatingMethodMixin


class ModelRepo(
    CreationMethodMixin,
    DeletionMethodMixin,
    RetrivingMethodMixin,
    UpdatingMethodMixin,
):
    """Class for model repository."""

    def __init__(self, sa_engine, sa_session_maker, model_klass):
        """Initializing with specific model."""
        self._model_klass = model_klass
        self._engine = sa_engine
        self._session_maker = sa_session_maker
