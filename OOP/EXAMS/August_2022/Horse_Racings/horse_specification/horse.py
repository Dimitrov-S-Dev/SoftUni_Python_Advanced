from abc import ABC, abstractmethod
from OOP.EXAMS.August_2022.Horse_Racings.core.validator import Validator


class Horse(ABC):
    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    @abstractmethod
    def max_speed(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_value_is_lt_min_value(
            len(value),
            4,
            f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        Validator.raise_if_value_gt_max_value(
            value,
            self.max_speed,
            "Horse speed is too high!")
        self.__speed = value

    @abstractmethod
    def train(self):
        pass
