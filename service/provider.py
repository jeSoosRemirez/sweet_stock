"""Business logic for managing providers."""

from models import Provider
from repository.repos import ProviderRepo
from schemas.provider import ProviderCreate, ProviderUpdate
from utils.pydantic_encoder import pyd_to_dict
from typing import Optional


class ProviderService:
    """Service class for provider management."""

    @classmethod
    async def create_provider(
        cls,
        body: ProviderCreate,
    ) -> Provider:
        """Create a new provider record."""
        provider = await ProviderRepo.create_one(pyd_to_dict(body))
        return provider

    @classmethod
    async def get_provider(
        cls,
        provider_id: str,
    ) -> Optional[Provider]:
        """Retrieve a provider record by its ID."""
        provider = await ProviderRepo.retrieve_by_id(id_value=provider_id)
        if not provider:
            raise ValueError(f"Provider with ID {provider_id} not found.")
        return provider

    @classmethod
    async def list_providers(
        cls,
    ) -> list[Provider]:
        """Retrieve a provider record by its ID."""
        provider = await ProviderRepo.retrieve()
        return provider

    @classmethod
    async def update_provider(
        cls,
        provider_id: str,
        body: ProviderUpdate,
    ) -> Provider:
        """Update an existing provider record."""
        existing_provider = await ProviderRepo.retrieve_by_id(id_value=provider_id)
        if not existing_provider:
            raise ValueError(f"Provider with ID {provider_id} not found.")

        updated_provider = await ProviderRepo.update_by_id(
            id_value=provider_id,
            **pyd_to_dict(body),
        )
        return updated_provider

    @classmethod
    async def delete_provider(
        cls,
        provider_id: str,
    ) -> Provider:
        """Delete a provider record by its ID."""
        provider = await ProviderRepo.retrieve_by_id(id_value=provider_id)
        if not provider:
            raise ValueError(f"Provider with ID {provider_id} not found.")

        deleted_provider = await ProviderRepo.delete_by_id(id_value=provider_id)
        return deleted_provider
