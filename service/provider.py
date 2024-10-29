"""Business-logic for Providers."""

from models import Provider
from repository.provider import ProviderRepo
from schemas.provider import CreateProviderSchema, UpdateProviderSchema
from utils.pydantic_encoder import pyd_to_dict


class ProviderService:
    """Class for Providers business-logic."""

    @classmethod
    async def create_provider(
        cls,
        body: CreateProviderSchema,
    ) -> Provider:
        """Create provider record."""
        provider = await ProviderRepo.create_one(
            pyd_to_dict(body),
        )
        return provider

    @classmethod
    async def get_provider(
        cls,
        provider_id: str,
    ) -> Provider:
        """Get provider record."""
        provider = await ProviderRepo.retrieve_by_id(id_value=provider_id)
        return provider

    @classmethod
    async def update_provider(
        cls,
        provider_id: str,
        body: UpdateProviderSchema,
    ) -> Provider:
        """Update provider record."""
        provider = await ProviderRepo.update_by_id(
            provider_id,
            **body,
        )
        return provider

    @classmethod
    async def delete_provider(
        cls,
        provider_id: str,
    ) -> Provider:
        """Update provider record."""
        provider = await ProviderRepo.delete_by_id(id_value=provider_id)
        return provider
