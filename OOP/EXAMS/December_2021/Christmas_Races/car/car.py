from abc import ABC, abstractmethod

from OOP.EXAMS.December_2021.Christmas_Races.core.validator import Validator


class Car(ABC):
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    @abstractmethod
    def min_speed_limit(self):
        pass

    @property
    @abstractmethod
    def max_speed_limit(self):
        pass

    @property
    @abstractmethod
    def invalid_speed_limit_message(self):
        pass

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        Validator.raise_if_less_then_four_symbols(
            value,
            f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        Validator.raise_if_invalid_speed_limit(
            value,
            self.min_speed_limit,
            self.max_speed_limit,
            self.invalid_speed_limit_message())
        self.__speed_limit = value
