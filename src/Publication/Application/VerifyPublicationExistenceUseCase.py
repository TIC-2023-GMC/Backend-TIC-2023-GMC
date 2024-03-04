from src.Publication.AdoptionPublication.Application.GetAdoptionByIdUseCase import (
    GetAdoptionByIdUseCase,
)
from src.Publication.ExperiencePublication.Application.GetExperienceByIdUseCase import (
    GetExperienceByIdUseCase,
)


class VerifyPublicationExistenceUseCase:
    def __init__(self):
        self.get_adoption_by_id = GetAdoptionByIdUseCase()
        self.get_experience_by_id = GetExperienceByIdUseCase()

    def execute(self, pub_id: str) -> bool:
        pub_adoption = self.get_adoption_by_id.execute(pub_id)
        pub_experience = self.get_experience_by_id.execute(pub_id)

        return pub_adoption or pub_experience
