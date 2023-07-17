from fastapi import APIRouter
from Publication.AdoptionPublication.Infrastructure.AdoptionFastAPIController import (
    router,
)

api_router = APIRouter()

api_router.include_router(router, prefix="/adoptions", tags=["adoptions"])
