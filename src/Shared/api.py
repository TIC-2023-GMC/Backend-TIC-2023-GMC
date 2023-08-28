from fastapi import APIRouter

from src.Publication.AdoptionPublication.Infrastructure.FastAPIAdoptionController import (
    router as adoption_router,
)
from src.Publication.ExperiencePublication.Infrastructure.FastAPIExperienceController import (
    router as experience_router,
)

from src.Photo.Infrastructure.FastAPIPhotoController import router as photo_router

from src.Parish.Infrastructure.FastAPIParishController import router as parish_router
from src.User.Infrastructure.FastAPIUserController import router as user_router
from src.Match.QuizGameMatch.Infrastructure.FastAPIQuizGameMatchController import (
    router as quiz_game_match_router,
)
from src.Game.Infraestructure.FastAPIGameController import (
    router as game_router,
)
from src.Interaction.Comment.Infrastructure.FastAPICommentController import (
    router as comment_router,
)
from src.Interaction.Like.Infrastructure.FastAPILikeController import router as like_router

api_router = APIRouter()

api_router.include_router(adoption_router, prefix="/adoptions", tags=["adoptions"])
api_router.include_router(
    experience_router, prefix="/experiences", tags=["experiences"]
)
api_router.include_router(comment_router, prefix="/comments", tags=["comment"])
api_router.include_router(user_router, prefix="/user", tags=["user"])
api_router.include_router(photo_router, prefix="/photo", tags=["photo"])
api_router.include_router(parish_router, prefix="/parish", tags=["parish"])
api_router.include_router(game_router, prefix="/game", tags=["game"])
api_router.include_router(quiz_game_match_router, prefix="/match", tags=["match"])
api_router.include_router(like_router, prefix="/like", tags=["like"])
