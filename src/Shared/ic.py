import inject
from src.Interaction.Comment.Infrastructure.MongoDBCommentRepository import (
    MongoDBCommentRepository,
)
from src.Interaction.Comment.Domain.CommentRepository import CommentRepository
from src.Game.Domain.GameRepository import GameRepository
from src.Game.Infraestructure.MongoDBGameRepository import MongoDBGameRepository
from src.Interaction.Like.Domain.LikeRepository import LikeRepository
from src.Interaction.Like.Infrastructure.MongoDBLikeRepository import (
    MongoDBLikeRepository,
)
from src.Match.QuizGameMatch.Domain.QuizGameMatchRepository import (
    QuizGameMatchRepository,
)
from src.Match.QuizGameMatch.Infrastructure.MongoDBQuizGameMatchRepository import (
    MongoDBQuizGameMatchRepository,
)
from src.User.Infrastructure.MongoDBUserRepository import MongoDBUserRepository
from src.User.Domain.UserRepository import UserRepository
from src.Parish.Infrastructure.MongoDBParishRepository import MongoDBParishRepository
from src.Parish.Domain.ParishRepository import ParishRepository
from src.Photo.Domain.PhotoRepository import PhotoRepository
from src.Photo.Infrastructure.FirebasePhotoRepository import FirebasePhotoRepository


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
            LikeRepository,
            MongoDBLikeRepository(),
        )

    inject.configure_once(configure)
