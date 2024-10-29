"""Endpoints for the storage."""

from typing import Annotated
from fastapi import APIRouter, Query
from schemas.storage import (
    StorageSchema,
    CreateStorageSchema,
)
from service.storage import StorageService

router = APIRouter(prefix="/storage", tags=["storage"])


@router.post("")
async def create_storage(body: CreateStorageSchema) -> StorageSchema:
    """Create method for Storage model."""
    storage = await StorageService.create_storage(
        body=body,
    )

    if not storage:
        return {"message": "Something went wrong."}

    return storage


@router.get("/{id}")
async def get_storage(storage_id: Annotated[str, Query(alias="id")]) -> StorageSchema:
    """Get method for Storage model."""
    storage = await StorageService.get_storage(
        storage_id=storage_id,
    )

    if not storage:
        return {"message": "Something went wrong."}

    return storage
