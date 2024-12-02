from fastapi import APIRouter, HTTPException
from schemas.order import OrderCreate, OrderRetrieve, OrderUpdate
from service.order import OrderService

# Initialize the router with a prefix and tags
router = APIRouter(prefix="/order", tags=["order"])


# Create an order
@router.post("/", response_model=OrderRetrieve)
async def create_order(body: OrderCreate):
    """Create a new order."""
    try:
        # Call the service method to create the order
        order = await OrderService.create_order(body)
        return order
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# Get an order by ID
@router.get("/{order_id}", response_model=OrderRetrieve)
async def get_order(order_id: str):
    """Get an order by its ID."""
    try:
        # Call the service method to get the order
        order = await OrderService.get_order(order_id)
        return order
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/", response_model=list[OrderRetrieve])
async def list_orders():
    """Get an order by its ID."""
    try:
        # Call the service method to get the order
        order = await OrderService.list_orders()
        return order
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# Update an order by ID
@router.put("/{order_id}", response_model=OrderRetrieve)
async def update_order(order_id: str, body: OrderUpdate):
    """Update an order by its ID."""
    try:
        # Call the service method to update the order
        order = await OrderService.update_order(order_id, body)
        return order
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# Delete an order by ID
@router.delete("/{order_id}", response_model=OrderRetrieve)
async def delete_order(order_id: str):
    """Delete an order by its ID."""
    try:
        # Call the service method to delete the order
        order = await OrderService.delete_order(order_id)
        return order
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
