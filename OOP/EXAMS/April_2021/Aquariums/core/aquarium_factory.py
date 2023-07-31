from OOP.EXAMS.April_2021.Aquariums.aquarium.freshwater_aquarium import FreshwaterAquarium
from OOP.EXAMS.April_2021.Aquariums.aquarium.saltwater_aquarium import SaltwaterAquarium


class AquariumFactory:
    VALID_TYPE = {"FreshwaterAquarium": FreshwaterAquarium, "SaltwaterAquarium": SaltwaterAquarium}

    def create_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.VALID_TYPE:
            raise ValueError(f"Invalid aquarium type.")
        return self.VALID_TYPE[aquarium_type](aquarium_name)
