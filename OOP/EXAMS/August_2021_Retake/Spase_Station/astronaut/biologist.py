from OOP.EXAMS.August_2021_Retake.Spase_Station.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    def __init__(self, name: str):
        super().__init__(name, 70)

    def breathe(self):
        self.oxygen -= 5
