from OOP.EXAMS.August_2022.Horse_Racings.horse_specification.horse import Horse


class Appaloosa(Horse):
    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def max_speed(self):
        return 120

    def train(self):
        self.speed = min(self.speed + 2, self.max_speed)