from OOP.EXAMS.August_2021.Baked_Delicacies.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    PORTION = 200

    def __init__(self, name: str, price: float):
        super().__init__(name, self.PORTION, price)
