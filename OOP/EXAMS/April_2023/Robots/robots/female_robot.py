from OOP.EXAMS.April_2023.Robots.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    WEIGHT = 7

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, self.WEIGHT)
        self.weight = self.WEIGHT

    def eating(self):
        self.weight += 1
