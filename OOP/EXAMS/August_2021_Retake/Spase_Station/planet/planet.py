from OOP.EXAMS.August_2021_Retake.Spase_Station.core.validator import Validator


class Planet:
    def __init__(self, name: str):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_empty_string_or_w_spaces(
            value,
            "Planet name cannot be empty string or whitespace!")
        self.__name = value

    def pick_item(self):
        return self.items.pop()
