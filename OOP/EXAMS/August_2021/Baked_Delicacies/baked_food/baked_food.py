from abc import ABC, abstractmethod

from OOP.EXAMS.August_2021.Baked_Delicacies.core.validator import Validator


class BakedFood(ABC):
    @abstractmethod
    def __init__(self, name: str, portion: float, price: float):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty_or_white_space(
            value,
            f"Name cannot be empty string or white space!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.raise_if_number_is_less_or_equal_to_zero(
            value,
            f"Price cannot be less than or equal to zero!")
        self.__price = value

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"
