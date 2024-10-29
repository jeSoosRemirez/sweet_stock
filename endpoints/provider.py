"""Endpoints for the provider."""

from typing import Annotated
from fastapi import APIRouter, Query
from schemas.provider import (
    ProviderSchema,
    CreateProviderSchema,
)
from service.provider import ProviderService

router = APIRouter(prefix="/provider", tags=["provider"])


@router.post("")
async def create_provider(body: CreateProviderSchema) -> ProviderSchema:
    """Create method for Provider model."""
    provider = await ProviderService.create_provider(
        body=body,
    )

    if not provider:
        return {"message": "Something went wrong."}

    return provider


@router.get("/{id}")
async def get_provider(
    provider_id: Annotated[str, Query(alias="id")]
) -> ProviderSchema:
    """Get method for Provider model."""
    provider = await ProviderService.get_provider(
        provider_id=provider_id,
    )

    if not provider:
        return {"message": "Something went wrong."}

    return provider
