from Photo.Domain.Photo import Photo
from User.Domain.User import User


class UserFactory:
    @staticmethod
    def create(
        _id: int,
        first_name: str,
        last_name: str,
        mobile_phone: str,
        neighborhood: str,
        email: str,
        password: str,
        num_previous_pets: int,
        num_current_pets: int,
        outdoor_hours: int,
        house_space: int,
        has_yard: bool,
        main_pet_food: str,
        pet_expenses: int,
        motivation: str,
        favorite_adoption_publications: list,
        photo: Photo,
    ) -> User:
        return User(
            _id=_id,
            first_name=first_name,
            last_name=last_name,
            mobile_phone=mobile_phone,
            neighborhood=neighborhood,
            email=email,
            password=password,
            num_previous_pets=num_previous_pets,
            num_current_pets=num_current_pets,
            outdoor_hours=outdoor_hours,
            house_space=house_space,
            has_yard=has_yard,
            main_pet_food=main_pet_food,
            pet_expenses=pet_expenses,
            motivation=motivation,
            favorite_adoption_publications=favorite_adoption_publications,
            photo=photo,
        )
