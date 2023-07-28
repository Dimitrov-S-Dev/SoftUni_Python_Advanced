from project.core.validator import Validator


class Driver:
    def __init__(self, name: str):
        self.name = name
        self.car = None
        self.number_of_wins = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_empty_or_only_white_spaces(
            value,
            "Name should contain at least one character!")
        self.__name = value

    def win(self):
        self.number_of_wins += 1

