"""Business logic for managing user records."""

from models import User
from repository.repos import UserRepo
from schemas.user import UserCreate, UserUpdate
from utils.pydantic_encoder import pyd_to_dict


class UserService:
    """Service class for managing users."""

    @classmethod
    async def create_user(
        cls,
        body: UserCreate,
    ) -> User:
        """Create a new user record."""
        # Create user by passing the validated body to the repository
        user = await UserRepo.create_one(pyd_to_dict(body))
        return user

    @classmethod
    async def get_user(
        cls,
        user_id: str,
    ) -> User:
        """Retrieve a user record by its ID."""
        user = await UserRepo.retrieve_by_id(id_value=user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found.")
        return user

    @classmethod
    async def list_users(
        cls,
    ) -> User:
        """Retrieve a user record by its ID."""
        user = await UserRepo.retrieve()
        return user

    @classmethod
    async def update_user(
        cls,
        user_id: str,
        body: UserUpdate,
    ) -> User:
        """Update an existing user record."""
        # Retrieve the user to ensure it exists
        user = await UserRepo.retrieve_by_id(id_value=user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found.")

        # Update the user with the provided data
        updated_user = await UserRepo.update_by_id(
            user_id,
            **pyd_to_dict(body),
        )
        return updated_user

    @classmethod
    async def delete_user(
        cls,
        user_id: str,
    ) -> User:
        """Delete a user record by its ID."""
        # Ensure the user exists before deleting
        user = await UserRepo.retrieve_by_id(id_value=user_id)
        if not user:
            raise ValueError(f"User with ID {user_id} not found.")

        # Proceed with the deletion
        deleted_user = await UserRepo.delete_by_id(id_value=user_id)
        return deleted_user
