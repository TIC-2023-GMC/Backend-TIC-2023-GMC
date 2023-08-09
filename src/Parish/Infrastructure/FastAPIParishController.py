from fastapi import APIRouter
from src.Shared.Singleton import singleton
from src.Parish.Domain.Parish import Parish
from src.Parish.Application.ListParishesUseCase import ListParishesUseCase

from typing import List

router = APIRouter()


@singleton
class FastAPIParishController:
    def __init__(self):
        self.list_parishes = ListParishesUseCase()

    def list_parishes_endpoint(self) -> List[Parish]:
        return self.list_parishes.execute()


def get_adoption_controller() -> FastAPIParishController:
    return FastAPIParishController()


@router.get("/get_all", status_code=200)
def list_parish_endpoint() -> List[Parish]:
    return get_adoption_controller().list_parishes_endpoint()
