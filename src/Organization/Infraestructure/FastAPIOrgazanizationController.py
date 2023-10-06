from typing import List, Tuple
from fastapi import APIRouter, HTTPException
from src.Organization.Application.GetOrganizationUseCase import GetOrganizationUseCase
from src.Organization.Domain.Organization import Organization

from src.Shared.Singleton import singleton


router = APIRouter()


@singleton
class FastAPIOrganizationController:
    def __init__(self):
        self.get_organization_use_case = GetOrganizationUseCase()

    def get_organizations_endpoint(
        self, page_number: int, page_size: int
    ) -> Tuple[List[Organization], int]:
        return self.get_organization_use_case.execute(
            page_numer=page_number, page_size=page_size
        )


def get_organization_controller() -> FastAPIOrganizationController:
    return FastAPIOrganizationController()


@router.get("/get_organizations", status_code=200)
def get_all_organizations_endpoint(
    page_number: int, page_size: int
) -> Tuple[List[Organization], int]:
    try:
        return get_organization_controller().get_organizations_endpoint(
            page_number=page_number, page_size=page_size
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
