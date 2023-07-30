from OOP.EXAMS.April_2022.Medieval_Games.supply.supply import Supply


class Food(Supply):
    def __init__(self, name: str, energy=25):
        super().__init__(name, energy)
