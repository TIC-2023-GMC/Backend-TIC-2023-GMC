from Publication.Domain.Publication import Publication


class AdoptionPublication(Publication):
    pet_size: str
    pet_breed: str
    pet_age: float
    pet_sex: bool
    pet_location: str
    sterilized: bool
    vaccination_card: bool
