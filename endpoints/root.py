"""Root fastapi router."""

import importlib

from fastapi import APIRouter

root_router = APIRouter(prefix="/api", tags=["all"])
modules = (
    "product",
    "provider",
    "storage",
)


for module_name in modules:
    module = importlib.import_module(f"endpoints.{module_name}")
    root_router.include_router(module.router)
