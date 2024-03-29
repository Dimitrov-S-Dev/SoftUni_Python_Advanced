from OOP.Exam_Prep.Aug_2022.Part_1.Horse_Racings.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    SPEED_INCREASE = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        self.speed = min(self.speed + self.SPEED_INCREASE, self.MAX_SPEED)

