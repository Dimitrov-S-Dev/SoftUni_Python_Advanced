from abc import ABC, abstractmethod

from project.core.validator import Validator


class Astronaut(ABC):
    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_empty_string_or_w_spaces(
            value,
            "Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= 10

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    def add_item(self, item):
        self.backpack.append(item)

    def __str__(self):
        output = f"Name: {self.name}" + "\n"
        output += f"Oxygen: {self.oxygen}" + "\n"
        output += f"Backpack items: {', '.join(self.backpack) if len(self.backpack) > 0 else 'none'}"
        return output
