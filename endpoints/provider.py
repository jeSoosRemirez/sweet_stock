from fastapi import APIRouter, HTTPException
from schemas.provider import ProviderCreate, ProviderRetrieve, ProviderUpdate
from service.provider import ProviderService

# Initialize the router
router = APIRouter(prefix="/provider", tags=["provider"])


# Create a provider
@router.post("/", response_model=ProviderRetrieve)
async def create_provider(body: ProviderCreate):
    """Create a new provider."""
    try:
        # Call the service method to create the provider
        provider = await ProviderService.create_provider(body)
        return provider
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# Get a provider by ID
@router.get("/{provider_id}", response_model=ProviderRetrieve)
async def get_provider(provider_id: str):
    """Get a provider by its ID."""
    try:
        # Call the service method to get the provider
        provider = await ProviderService.get_provider(provider_id)
        return provider
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/", response_model=list[ProviderRetrieve])
async def list_providers():
    """Get a provider by its ID."""
    try:
        # Call the service method to get the provider
        provider = await ProviderService.list_providers()
        return provider
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# Update a provider by ID
@router.put("/{provider_id}", response_model=ProviderRetrieve)
async def update_provider(provider_id: str, body: ProviderUpdate):
    """Update a provider by its ID."""
    try:
        # Call the service method to update the provider
        provider = await ProviderService.update_provider(provider_id, body)
        return provider
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# Delete a provider by ID
@router.delete("/{provider_id}", response_model=ProviderRetrieve)
async def delete_provider(provider_id: str):
    """Delete a provider by its ID."""
    try:
        # Call the service method to delete the provider
        provider = await ProviderService.delete_provider(provider_id)
        return provider
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
