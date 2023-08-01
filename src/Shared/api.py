from fastapi import APIRouter

from src.Publication.AdoptionPublication.Infrastructure.AdoptionFastAPIController import (
    router as adoption_router,
)
from src.Publication.ExperiencePublication.Infrastructure.ExperienceFastAPIController import (
    router as experience_router,
)

from src.Photo.Infrastructure.PhotoFastAPIController import router as photo_router

from src.Parish.Infrastructure.ParishFastAPIController import router as parish_router
from src.User.Infrastructure.UserFastAPIController import router as user_router
from src.Game.QuizGame.Infrastructure.QuizGameFastAPIController import (
    router as quiz_game_router,
)

api_router = APIRouter()

api_router.include_router(adoption_router, prefix="/adoptions", tags=["adoptions"])
api_router.include_router(photo_router, prefix="/photo", tags=["photo"])
api_router.include_router(
    experience_router, prefix="/experiences", tags=["experiences"]
)
api_router.include_router(user_router, prefix="/user", tags=["user"])
api_router.include_router(parish_router, prefix="/parish", tags=["parish"])
api_router.include_router(quiz_game_router, prefix="/game", tags=["game"])
