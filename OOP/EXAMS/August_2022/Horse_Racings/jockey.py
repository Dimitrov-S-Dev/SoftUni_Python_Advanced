from OOP.EXAMS.August_2022.Horse_Racings.core.validator import Validator
class Jockey:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.horse = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_empty_string_or_w_space(
            value,
            "Name should contain at least one character!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.raise_if_value_is_lt_min_value(
            value,
            18,
            "Jockeys must be at least 18 to participate in the race!")
        self.__age = value
