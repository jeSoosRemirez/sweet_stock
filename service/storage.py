"""Business logic for managing storage records."""

from models import Storage
from repository.repos import StorageRepo
from schemas.storage import StorageCreate, StorageUpdate
from utils.pydantic_encoder import pyd_to_dict
from typing import Optional


class StorageService:
    """Service class for storage management."""

    @classmethod
    async def create_storage(
        cls,
        body: StorageCreate,
    ) -> Storage:
        """Create a new storage record."""
        storage = await StorageRepo.create_one(pyd_to_dict(body))
        return storage

    @classmethod
    async def get_storage(
        cls,
        storage_id: str,
    ) -> Optional[Storage]:
        """Retrieve a storage record by its ID."""
        storage = await StorageRepo.retrieve_by_id(id_value=storage_id)
        if not storage:
            raise ValueError(f"Storage with ID {storage_id} not found.")
        return storage

    @classmethod
    async def list_storages(
        cls,
    ) -> Optional[Storage]:
        """Retrieve a storage record by its ID."""
        storage = await StorageRepo.retrieve()
        return storage

    @classmethod
    async def update_storage(
        cls,
        storage_id: str,
        body: StorageUpdate,
    ) -> Storage:
        """Update an existing storage record."""
        existing_storage = await StorageRepo.retrieve_by_id(id_value=storage_id)
        if not existing_storage:
            raise ValueError(f"Storage with ID {storage_id} not found.")

        updated_storage = await StorageRepo.update_by_id(
            id_value=storage_id,
            **pyd_to_dict(body),
        )
        return updated_storage

    @classmethod
    async def delete_storage(
        cls,
        storage_id: str,
    ) -> Storage:
        """Delete a storage record by its ID."""
        storage = await StorageRepo.retrieve_by_id(id_value=storage_id)
        if not storage:
            raise ValueError(f"Storage with ID {storage_id} not found.")

        deleted_storage = await StorageRepo.delete_by_id(id_value=storage_id)
        return deleted_storage
