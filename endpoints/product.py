from fastapi import APIRouter, HTTPException
from schemas.product import ProductCreate, ProductRetrieve, ProductUpdate
from service.product import ProductService

# Initialize the router
router = APIRouter(prefix="/product", tags=["product"])


# Create a product
@router.post("/", response_model=ProductRetrieve)
async def create_product(body: ProductCreate):
    """Create a new product."""
    try:
        # Call the service method to create the product
        product = await ProductService.create_product(body)
        return product
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# Get a product by ID
@router.get("/{product_id}", response_model=ProductRetrieve)
async def get_product(product_id: str):
    """Get a product by its ID."""
    try:
        # Call the service method to get the product
        product = await ProductService.get_product(product_id)
        return product
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/", response_model=list[ProductRetrieve])
async def list_products():
    """Get a product by its ID."""
    try:
        # Call the service method to get the product
        product = await ProductService.list_products()
        return product
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# Update a product by ID
@router.put("/{product_id}", response_model=ProductRetrieve)
async def update_product(product_id: str, body: ProductUpdate):
    """Update a product by its ID."""
    try:
        # Call the service method to update the product
        product = await ProductService.update_product(product_id, body)
        return product
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# Delete a product by ID
@router.delete("/{product_id}", response_model=ProductRetrieve)
async def delete_product(product_id: str):
    """Delete a product by its ID."""
    try:
        # Call the service method to delete the product
        product = await ProductService.delete_product(product_id)
        return product
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
