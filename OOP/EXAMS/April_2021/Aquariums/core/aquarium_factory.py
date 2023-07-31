from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium


class AquariumFactory:
    VALID_TYPE = {"FreshwaterAquarium": FreshwaterAquarium, "SaltwaterAquarium": SaltwaterAquarium}

    def create_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type in self.VALID_TYPE:
            return self.VALID_TYPE[aquarium_type](aquarium_name)
