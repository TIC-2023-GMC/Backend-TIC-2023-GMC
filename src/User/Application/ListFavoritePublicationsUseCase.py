import inject
from src.User.Domain.UserRepository import UserRepository
from typing import List

class ListFavoritePublicationsUseCase:
    @inject.autoparams()
    def __init__(self, user_repository:UserRepository):
        self.user_repository = user_repository

    def execute(self, favorite_adoption_publications: List[str]):
        return self.user_repository.list_favorite_publications(favorite_adoption_publications=favorite_adoption_publications)
