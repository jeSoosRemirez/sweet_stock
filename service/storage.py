"""Business-logic for Providers."""

from models import Storage
from repository.storage import StorageRepo
from schemas.storage import CreateStorageSchema, UpdateStorageSchema
from utils.pydantic_encoder import pyd_to_dict


class StorageService:
    """Class for Providers business-logic."""

    @classmethod
    async def create_storage(
        cls,
        body: CreateStorageSchema,
    ) -> Storage:
        """Create storage record."""
        storage = await StorageRepo.create_one(
            pyd_to_dict(body),
        )
        return storage

    @classmethod
    async def get_storage(
        cls,
        storage_id: str,
    ) -> Storage:
        """Get storage record."""
        storage = await StorageRepo.retrieve_by_id(id_value=storage_id)
        return storage

    @classmethod
    async def update_storage(
        cls,
        storage_id: str,
        body: UpdateStorageSchema,
    ) -> Storage:
        """Update storage record."""
        storage = await StorageRepo.update_by_id(
            storage_id,
            **body,
        )
        return storage

    @classmethod
    async def delete_storage(
        cls,
        storage_id: str,
    ) -> Storage:
        """Delete storage record."""
        storage = await StorageRepo.delete_by_id(id_value=storage_id)
        return storage
