from OOP.EXAMS.August_2022.Horse_Racings.core.validator import Validator


class HorseRace:
    def __init__(self, race_type: str):
        self.race_type = race_type
        self.jockeys = []

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value):
        Validator.raise_if_skill_not_in_available(
            value,
            ["Winter", "Spring", "Autumn", "Summer"],
            "Race type does not exist!")
        self.__race_type = value
