from fastapi import APIRouter

from src.Publication.AdoptionPublication.Infrastructure.AdoptionFastAPIController import (
    router as adoption_router,
)

from src.Photo.Infrastructure.PhotoFastAPIController import router as photo_router

api_router = APIRouter()

api_router.include_router(adoption_router, prefix="/adoptions", tags=["adoptions"])
api_router.include_router(photo_router, prefix="/photo", tags=["photo"])
