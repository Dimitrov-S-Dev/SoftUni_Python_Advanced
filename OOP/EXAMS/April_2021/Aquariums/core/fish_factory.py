from OOP.EXAMS.April_2021.Aquariums.fish.freshwater_fish import FreshwaterFish
from OOP.EXAMS.April_2021.Aquariums.fish.saltwater_fish import SaltwaterFish


class FishFactory:
    VALID_TYPES = {"FreshwaterFish": FreshwaterFish, "SaltwaterFish": SaltwaterFish}

    def create_fish(self, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type in self.VALID_TYPES:
            return self.VALID_TYPES[fish_type](fish_name, fish_species, price)
