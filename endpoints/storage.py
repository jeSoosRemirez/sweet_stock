from fastapi import APIRouter, HTTPException
from schemas.storage import StorageCreate, StorageRetrieve, StorageUpdate
from service.storage import StorageService

# Initialize the router with a prefix and tags
router = APIRouter(prefix="/storage", tags=["storage"])


# Create a storage
@router.post("/", response_model=StorageRetrieve)
async def create_storage(body: StorageCreate):
    """Create a new storage."""
    try:
        # Call the service method to create the storage
        storage = await StorageService.create_storage(body)
        return storage
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# Get a storage by ID
@router.get("/{storage_id}", response_model=StorageRetrieve)
async def get_storage(storage_id: str):
    """Get a storage by its ID."""
    try:
        # Call the service method to get the storage
        storage = await StorageService.get_storage(storage_id)
        return storage
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/", response_model=list[StorageRetrieve])
async def list_storages():
    """Get a storage by its ID."""
    try:
        # Call the service method to get the storage
        storage = await StorageService.list_storages()
        return storage
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# Update a storage by ID
@router.put("/{storage_id}", response_model=StorageRetrieve)
async def update_storage(storage_id: str, body: StorageUpdate):
    """Update a storage by its ID."""
    try:
        # Call the service method to update the storage
        storage = await StorageService.update_storage(storage_id, body)
        return storage
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# Delete a storage by ID
@router.delete("/{storage_id}", response_model=StorageRetrieve)
async def delete_storage(storage_id: str):
    """Delete a storage by its ID."""
    try:
        # Call the service method to delete the storage
        storage = await StorageService.delete_storage(storage_id)
        return storage
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
