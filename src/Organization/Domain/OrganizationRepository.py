from abc import ABC, abstractmethod
from typing import List, Tuple

from src.Organization.Domain.Organization import Organization


class OrganizationRepository(ABC):
    @abstractmethod
    def get_all(
        self, page_number: int, page_size: int
    ) -> Tuple[List[Organization], int]:
        pass
