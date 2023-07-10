from Publication.Publication import Publication

class AdoptionPublication(Publication):
    def __init__(self):
        self.pet_size = None
        self.pet_breed = None
        self.pet_age = None
        self.pet_sex = None
        self.pet_location = None
        self.sterilized = None
        self.vaccination_card = None

