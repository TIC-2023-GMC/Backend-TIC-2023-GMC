from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from src.Interaction.Like.Application.AddLikeAdoptionPublicationUseCase import AddLikeAdoptionPublicationUseCase
from src.Shared.Singleton import singleton
router = APIRouter()

@singleton
class FastAPILikeController:
    def __init__(self):
        self.add_like_adoption_pub_use_case = AddLikeAdoptionPublicationUseCase()

    def add_like_adoption_pub(self, pub_id: str, user_id: str) -> None:
        self.add_like_adoption_pub_use_case.execute(pub_id=pub_id, user_id=user_id)
    
def like_controller()-> FastAPILikeController:
    return FastAPILikeController()

@router.post("/add_like_adoption_pub", status_code=200)
def add_like_adoption_pub_endpoint(user_id:str, pub_id:str) -> None:
    try:
        like_controller().add_like_adoption_pub(pub_id=pub_id, user_id=user_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))	


