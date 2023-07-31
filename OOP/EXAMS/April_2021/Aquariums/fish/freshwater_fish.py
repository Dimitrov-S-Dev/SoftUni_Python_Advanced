from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    SIZE = 3
    SIZE_INCREMENT = 3

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.SIZE, price)

    def eat(self):
        self.size += self.SIZE_INCREMENT
