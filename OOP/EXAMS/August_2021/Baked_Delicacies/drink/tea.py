from OOP.EXAMS.August_2021.Baked_Delicacies.drink.drink import Drink


class Tea(Drink):
    PRICE = 2.50

    def __init__(self, name: str, portion: int, brand: str):
        super().__init__(name, portion, self.PRICE, brand)
