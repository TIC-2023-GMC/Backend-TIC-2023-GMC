from typing import Optional
from src.Photo.Domain.Photo import Photo
from src.Shared.Model import Model


class User(Model):
    _id: Optional[str]
    first_name: str
    last_name: str
    mobile_phone: str
    neighborhood: str
    email: str
    password: str
    num_previous_pets: int
    num_current_pets: int
    outdoor_hours: int
    house_space: int
    has_yard: bool
    main_pet_food: str
    pet_expenses: int
    motivation: str
    favorite_adoption_publications: list
    photo: Photo
