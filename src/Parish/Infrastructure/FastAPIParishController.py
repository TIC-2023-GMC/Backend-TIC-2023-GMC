from typing import List

from fastapi import APIRouter, HTTPException

from src.Parish.Application.ListParishesUseCase import ListParishesUseCase
from src.Parish.Domain.Parish import Parish
from src.Shared.Singleton import singleton

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
    try:
        return get_adoption_controller().list_parishes_endpoint()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
