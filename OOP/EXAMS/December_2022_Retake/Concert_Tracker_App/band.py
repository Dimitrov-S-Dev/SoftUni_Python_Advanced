from OOP.EXAMS.December_2022_Retake.Concert_Tracker_App.core.validator import Validator


class Band:
    def __init__(self, name: str):
        self.name = name
        self.members = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_empty_string_or_w_space(
            value,
            "Band name should contain at least one character!")
        self.__name = value

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member):
        self.members.remove(member)

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."
