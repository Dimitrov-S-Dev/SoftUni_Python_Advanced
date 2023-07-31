from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    SIZE = 5
    SIZE_INCREMENT = 2

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.SIZE, price)

    def eat(self):
        self.size += self.SIZE_INCREMENT
