from OOP.Exam_Prep.Aug_2022.Part_1.Horse_Racings.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    SPEED_INCREASE = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        self.speed = min(self.speed + self.SPEED_INCREASE, self.MAX_SPEED)
