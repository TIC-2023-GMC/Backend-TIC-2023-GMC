from fastapi import APIRouter, Depends

from src.Game.Infraestructure.FastAPIGameController import router as game_router
from src.Interaction.Comment.Infrastructure.FastAPICommentController import (
    router as comment_router,
)
from src.Interaction.Like.Infrastructure.FastAPILikeController import (
    router as like_router,
)
from src.Match.QuizGameMatch.Infrastructure.FastAPIQuizGameMatchController import (
    router as quiz_game_match_router,
)
from src.Match.WordleGameMatch.Infrastructure.FastAPIWordleMatchController import (
    router as wordle_router,
)
from src.Match.WordSearchGameMatch.Infrastructure.FastAPIWordSearchGameMatchController import (
    router as word_search_game_match_router,
)
from src.Organization.Infraestructure.FastAPIOrganizationController import (
    router as organization_router,
)
from src.Parish.Infrastructure.FastAPIParishController import router as parish_router
from src.Photo.Infrastructure.FastAPIPhotoController import router as photo_router
from src.Publication.AdoptionPublication.Infrastructure.FastAPIAdoptionController import (
    router as adoption_router,
)
from src.Publication.ExperiencePublication.Infrastructure.FastAPIExperienceController import (
    router as experience_router,
)
from src.User.Infrastructure.FastAPIUserController import (
    auth_router,
    get_current_active_user,
)
from src.User.Infrastructure.FastAPIUserController import router as user_router

unprotected_router = APIRouter()
unprotected_router.include_router(auth_router, prefix="/user", tags=["user"])
unprotected_router.include_router(parish_router, prefix="/parish", tags=["parish"])
unprotected_router.include_router(photo_router, prefix="/photo", tags=["photo"])


protected_router = APIRouter(dependencies=[Depends(get_current_active_user)])

protected_router.include_router(
    adoption_router, prefix="/adoptions", tags=["adoptions"]
)
protected_router.include_router(
    experience_router, prefix="/experiences", tags=["experiences"]
)
protected_router.include_router(comment_router, prefix="/comments", tags=["comment"])
protected_router.include_router(user_router, prefix="/user", tags=["user"])
protected_router.include_router(game_router, prefix="/game", tags=["game"])
protected_router.include_router(quiz_game_match_router, prefix="/match", tags=["match"])
protected_router.include_router(
    word_search_game_match_router, prefix="/word_search_game", tags=["word_search_game"]
)
protected_router.include_router(like_router, prefix="/like", tags=["like"])
protected_router.include_router(
    organization_router, prefix="/organization", tags=["organization"]
)
protected_router.include_router(wordle_router, prefix="/wordle", tags=["wordle"])

api_router = APIRouter()
api_router.include_router(unprotected_router)
api_router.include_router(protected_router)
