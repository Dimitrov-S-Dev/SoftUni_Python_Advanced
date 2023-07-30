from OOP.EXAMS.April_2022.Medieval_Games.supply.supply import Supply


class Drink(Supply):
    ENERGY = 15

    def __init__(self, name: str):
        super().__init__(name, self.ENERGY)
