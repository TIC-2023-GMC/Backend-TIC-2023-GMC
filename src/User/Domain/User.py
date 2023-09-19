from datetime import datetime
from typing import List, Optional

from src.Photo.Domain.Photo import Photo
from src.Shared.Model import Model


class User(Model):
    _id: str
    first_name: str
    last_name: str
    mobile_phone: str
    neighborhood: str
    birth_date: datetime
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
    favorite_adoption_publications: Optional[List[str]]
    photo: Photo
