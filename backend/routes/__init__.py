"""Routes package for FastAPI API endpoints."""
from .tasks import router as tasks_router

__all__ = ["tasks_router"]
