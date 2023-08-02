from OOP.EXAMS.April_2021.Aquariums.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    CAPACITY = 50

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    @property
    def fish_type(self):
        return "FreshwaterFish"
