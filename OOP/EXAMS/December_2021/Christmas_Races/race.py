from OOP.EXAMS.December_2021.Christmas_Races.core.validator import Validator


class Race:
    def __init__(self, name: str):
        self.name = name
        self.drivers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_empty_string(
            value,
            "Name cannot be an empty string!")
        self.__name = value

