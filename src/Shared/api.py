from fastapi import APIRouter

from src.Publication.AdoptionPublication.Infrastructure.AdoptionFastAPIController import (
    router,
)

api_router = APIRouter()

api_router.include_router(router, prefix="/adoptions", tags=["adoptions"])
