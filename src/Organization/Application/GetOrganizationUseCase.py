from typing import List, Tuple
import inject
from src.Organization.Domain.Organization import Organization
from src.Organization.Domain.OrganizationRepository import OrganizationRepository


class GetOrganizationUseCase:
    @inject.autoparams()
    def __init__(self, repository: OrganizationRepository):
        self.repository = repository

    def execute(self, page_numer, page_size) -> Tuple[List[Organization], int]:
        return self.repository.get_organizations(
            page_number=page_numer, page_size=page_size
        )
