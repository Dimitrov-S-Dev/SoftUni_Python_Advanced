from OOP.EXAMS.December_2022.Christmas_Pastry_Shop.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    def __init__(self, name: str, price: float):
        super().__init__(name, 200, price)
