from OOP.EXAMS.December_2022.Christmas_Pastry_Shop.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    def __init__(self, name: str, price: float):
        super().__init__(name, 250, price)
