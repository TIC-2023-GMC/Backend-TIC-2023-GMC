import inject
from typing import List, Tuple
from datetime import date
from src.Parish.Domain.Parish import Parish
from src.Parish.Domain.ParishRepository import ParishRepository


class ListParishesUseCase:
    @inject.autoparams()
    def __init__(self, parish_repository: ParishRepository):
        self.parish_repository = parish_repository

    def execute(self) -> List[Parish]:
        return self.parish_repository.get_all()
