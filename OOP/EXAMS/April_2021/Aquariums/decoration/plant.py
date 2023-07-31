from OOP.EXAMS.April_2021.Aquariums.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):
    COMFORT = 5
    PRICE = 10

    def __init__(self):
        super().__init__(self.COMFORT, self.PRICE)
