from datetime import datetime
from typing import List, Tuple

import inject

from src.Publication.Domain.PublicationRepository import PublicationRepository
from src.Publication.ExperiencePublication.Domain.ExperiencePublication import (
    ExperiencePublication,
)
from src.Publication.ExperiencePublication.Infrastructure.MongoDBExperiencePublicationRepository import (
    MongoDBExperiencePublicationRepository,
)


class ListExperiencePublicationsUseCase:
    @inject.params(
        publication_repository=MongoDBExperiencePublicationRepository,
    )
    def __init__(self, publication_repository: PublicationRepository):
        self.publication_repository = publication_repository

    def execute(
        self,
        page_number,
        page_size,
        experience_date: datetime,
        species: str,
        user_id: str,
    ) -> Tuple[List[ExperiencePublication], int]:
        return self.publication_repository.get_all(
            page_number=page_number,
            page_size=page_size,
            date=experience_date,
            species=species,
            user_id=user_id,
        )
