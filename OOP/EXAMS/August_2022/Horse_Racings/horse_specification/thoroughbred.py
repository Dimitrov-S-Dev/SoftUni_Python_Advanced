from OOP.EXAMS.August_2022.Horse_Racings.horse_specification.horse import Horse


class Thoroughbred(Horse):
    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def max_speed(self):
        return 140

    def train(self):
        self.speed = min(self.speed + 3, self.max_speed)