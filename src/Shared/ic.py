import inject

from src.Game.Domain.GameRepository import GameRepository
from src.Game.Infraestructure.MongoDBGameRepository import MongoDBGameRepository
from src.Interaction.Comment.Domain.CommentRepository import CommentRepository
from src.Interaction.Comment.Infrastructure.MongoDBCommentRepository import (
    MongoDBCommentRepository,
)
from src.Match.QuizGameMatch.Domain.QuizGameMatchRepository import (
    QuizGameMatchRepository,
)
from src.Match.QuizGameMatch.Infrastructure.MongoDBQuizGameMatchRepository import (
    MongoDBQuizGameMatchRepository,
)
from src.Match.WordleGameMatch.Domain.WordleMatchRepository import WordleMatchRepository
from src.Match.WordleGameMatch.Infrastructure.MongoDBWordleRepository import (
    MongoDBWordleMatchRepository,
)
from src.Match.WordSearchGameMatch.Domain.WordSearchGameMatchRepository import (
    WordSearchGameMatchRepository,
)
from src.Match.WordSearchGameMatch.Infrastructure.MongoDBWordSearchGameMatchRepository import (
    MongoDBWordSearchGameMatchRepository,
)
from src.Organization.Domain.OrganizationRepository import OrganizationRepository
from src.Organization.Infraestructure.MongoDBOrganizationRepository import (
    MongoDBOrganizationRepository,
)
from src.Parish.Domain.ParishRepository import ParishRepository
from src.Parish.Infrastructure.MongoDBParishRepository import MongoDBParishRepository
from src.Photo.Domain.PhotoRepository import PhotoRepository
from src.Photo.Infrastructure.FirebasePhotoRepository import FirebasePhotoRepository
from src.User.Domain.AuthService import AuthService
from src.User.Domain.UserRepository import UserRepository
from src.User.Infrastructure.JWTAuthService import JWTAuthService
from src.User.Infrastructure.MongoDBUserRepository import MongoDBUserRepository


def configure_ic() -> None:
    def configure(binder: inject.Binder) -> None:
        binder.bind(
            PhotoRepository,
            FirebasePhotoRepository(),
        )
        binder.bind(
            ParishRepository,
            MongoDBParishRepository(),
        )
        binder.bind(
            UserRepository,
            MongoDBUserRepository(),
        )
        binder.bind(
            QuizGameMatchRepository,
            MongoDBQuizGameMatchRepository(),
        )
        binder.bind(
            GameRepository,
            MongoDBGameRepository(),
        )
        binder.bind(
            CommentRepository,
            MongoDBCommentRepository(),
        )
        binder.bind(
            AuthService,
            JWTAuthService(),
        )
        binder.bind(
            OrganizationRepository,
            MongoDBOrganizationRepository(),
        )
        binder.bind(
            WordSearchGameMatchRepository,
            MongoDBWordSearchGameMatchRepository(),
        )
        binder.bind(
            WordleMatchRepository,
            MongoDBWordleMatchRepository(),
        )

    inject.configure_once(configure)
