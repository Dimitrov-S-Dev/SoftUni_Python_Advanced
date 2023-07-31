from abc import ABC, abstractmethod

from OOP.EXAMS.April_2021.Aquariums.core.validator import Validator


class BaseFish(ABC):
    SIZE_INCREMENT = 5

    @abstractmethod
    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_empty_string(
            value,
            "Fish name cannot be an empty string.")
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        Validator.raise_if_empty_string(
            value,
            "Fish species cannot be an empty string.")
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.raise_if_lte_to_zero(
            value,
            "Price cannot be equal to or below zero.")
        self.__price = value

    def eat(self):
        self.size += self.SIZE_INCREMENT
