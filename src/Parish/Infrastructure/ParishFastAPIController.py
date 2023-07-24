from fastapi import APIRouter, Query
from src.Parish.Domain.Parish import Parish
from src.Parish.Application.ListParishesUseCase import ListParishesUseCase

from typing import List

router = APIRouter()


class ParishFastAPIController:
    def __init__(self):
        self.list_parishes = ListParishesUseCase()

    def list_parishes_endpoint(self):
        return self.list_parishes.execute()


# Dependency
def get_adoption_controller():
    return ParishFastAPIController()


@router.get("/get_all", status_code=200)
def list_adoptions_endpoint() -> List[Parish]:
    return get_adoption_controller().list_parishes_endpoint()
