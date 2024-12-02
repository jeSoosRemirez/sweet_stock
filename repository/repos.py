"""Module with model repos."""

from models import (
    Product,
    Provider,
    Supply,
    User,
    Storage,
    Order,
)
from models.base import ModelRepo


ProductRepo = ModelRepo(Product)
ProviderRepo = ModelRepo(Provider)
SupplyRepo = ModelRepo(Supply)
UserRepo = ModelRepo(User)
StorageRepo = ModelRepo(Storage)
OrderRepo = ModelRepo(Order)
