from project.core.aquarium_factory import AquariumFactory
from project.core.decoration_factory import DecorationFactory
from project.core.fish_factory import FishFactory
from project.decoration.decoration_repository import DecorationRepository


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

        self.aquarium_factory = AquariumFactory()
        self.decoration_factory = DecorationFactory()
        self.fish_factory = FishFactory()

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):

        aquarium = self.aquarium_factory.create_aquarium(aquarium_type, aquarium_name)
        if aquarium is None:
            return f"Invalid aquarium type."

        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):

        if decoration_type not in ["Ornament", "Plant"]:
            return "Invalid decoration type."

        decoration = self.decoration_factory.create_decoration(decoration_type)
        self.decorations_repository.decorations.append(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):

        index, decoration = self.__find_decoration_by_type(decoration_type)
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if aquarium is None:
            return

        aquarium.add_decoration(decoration)
        self.decorations_repository.decorations.pop(index)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):

        fish = self.fish_factory.create_fish(fish_type, fish_name, fish_species, price)
        if fish is None:
            return f"There isn't a fish of type {fish_type}."

        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if aquarium is None:
            return

        if aquarium.fish_type != fish_type:
            return f"Water not suitable."

        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):

        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if aquarium is None:
            return

        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):

        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if aquarium is None:
            return

        return aquarium.calculate_value()

    def report(self):
        output = ""
        for aquarium in self.aquariums:
            output += str(aquarium) + "\n"

        return output.strip()

    def __find_decoration_by_type(self, decoration_type):
        for index, decoration in enumerate(self.decorations_repository.decorations):
            if decoration.__class__.__name__ == decoration_type:
                return index, decoration
        return f"There isn't a decoration of type {decoration_type}."

    def __find_aquarium_by_name(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium
