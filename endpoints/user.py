from fastapi import APIRouter, HTTPException
from schemas.user import UserCreate, UserRetrieve, UserUpdate
from service.user import UserService

# Initialize the router with a prefix and tags
router = APIRouter(prefix="/user", tags=["user"])


# Create a user
@router.post("/", response_model=UserRetrieve)
async def create_user(body: UserCreate):
    """Create a new user."""
    try:
        # Call the service method to create the user
        user = await UserService.create_user(body)
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# Get a user by ID
@router.get("/{user_id}", response_model=UserRetrieve)
async def get_user(user_id: str):
    """Get a user by its ID."""
    try:
        # Call the service method to get the user
        user = await UserService.get_user(user_id)
        return user
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/", response_model=list[UserRetrieve])
async def list_user():
    """Get a user by its ID."""
    try:
        # Call the service method to get the user
        user = await UserService.list_users()
        return user
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# Update a user by ID
@router.put("/{user_id}", response_model=UserRetrieve)
async def update_user(user_id: str, body: UserUpdate):
    """Update a user by its ID."""
    try:
        # Call the service method to update the user
        user = await UserService.update_user(user_id, body)
        return user
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# Delete a user by ID
@router.delete("/{user_id}", response_model=UserRetrieve)
async def delete_user(user_id: str):
    """Delete a user by its ID."""
    try:
        # Call the service method to delete the user
        user = await UserService.delete_user(user_id)
        return user
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
