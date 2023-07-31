from abc import ABC, abstractmethod
from OOP.EXAMS.April_2021.Aquariums.core.validator import Validator


class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity

        self.decorations = []
        self.fish = []

    @property
    @abstractmethod
    def fish_type(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_empty_string(
            value,
            "Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum(d.comfort for d in self.decorations)

    def add_fish(self, fish):
        if self.capacity == len(self.fish):
            return "Not enough capacity."
        if self.fish_type != fish.__class.__name__:
            return f"Water not suitable."
        self.fish.append(fish)
        return f"Successfully added {self.fish_type} to {self.name}."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def calculate_value(self):
        value = sum(f.price for f in self.fish) + sum(d.price for d in self.decorations)
        return f"The value of Aquarium {self.name} is {value:.2f}."

    def __str__(self):
        fishes = " ".join([f.name for f in self.fish]) if self.fish else "none"
        return f"{self.name}:\n"\
               f"Fish: {fishes}\n" \
               f"Decorations: {len(self.decorations)}\n"\
               f"Comfort: {self.calculate_comfort()}"
