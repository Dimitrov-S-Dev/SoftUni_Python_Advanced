from abc import ABC, abstractmethod

from OOP.EXAMS.December_2022.Christmas_Pastry_Shop.core.validator import Validator


class Delicacy(ABC):
    @abstractmethod
    def __init__(self, name: str, portion: int, price: float):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_empty_string_or_w_space(
            value,
            "Name cannot be null or whitespace!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.raise_if_lte_zero(
            value,
            "Price cannot be less or equal to zero!")
        self.__price = value

    def details(self):
        return f"{self.__class__.__name__} {self.name}: {self.portion}g - {self.price:.2f}lv."
