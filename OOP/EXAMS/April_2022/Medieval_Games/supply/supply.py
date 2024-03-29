from abc import ABC, abstractmethod

from OOP.EXAMS.April_2022.Medieval_Games.core.validator import Validator


class Supply(ABC):
    @abstractmethod
    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_empty_string(value, "Name cannot be an empty string.")
        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        Validator.raise_if_number_not_in_range(value, 0, "Energy cannot be less than zero.")
        self.__energy = value

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"
