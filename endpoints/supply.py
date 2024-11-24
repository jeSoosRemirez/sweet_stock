from fastapi import APIRouter, HTTPException
from schemas.supply import SupplyCreate, SupplyRetrieve, SupplyUpdate
from service.supply import SupplyService

# Initialize the router with a prefix and tags
router = APIRouter(prefix="/supply", tags=["supply"])


# Create a supply
@router.post("/", response_model=SupplyRetrieve)
async def create_supply(body: SupplyCreate):
    """Create a new supply."""
    try:
        # Call the service method to create the supply
        supply = await SupplyService.create_supply(body)
        return supply
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# Get a supply by ID
@router.get("/{supply_id}", response_model=SupplyRetrieve)
async def get_supply(supply_id: str):
    """Get a supply by its ID."""
    try:
        # Call the service method to get the supply
        supply = await SupplyService.get_supply(supply_id)
        return supply
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/", response_model=list[SupplyRetrieve])
async def list_supplies():
    """Get a supply by its ID."""
    try:
        # Call the service method to get the supply
        supply = await SupplyService.list_supplies()
        return supply
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# Update a supply by ID
@router.put("/{supply_id}", response_model=SupplyRetrieve)
async def update_supply(supply_id: str, body: SupplyUpdate):
    """Update a supply by its ID."""
    try:
        # Call the service method to update the supply
        supply = await SupplyService.update_supply(supply_id, body)
        return supply
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# Delete a supply by ID
@router.delete("/{supply_id}", response_model=SupplyRetrieve)
async def delete_supply(supply_id: str):
    """Delete a supply by its ID."""
    try:
        # Call the service method to delete the supply
        supply = await SupplyService.delete_supply(supply_id)
        return supply
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
