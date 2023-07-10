from abc import ABC
from project.animal import Animal


class Dog(Animal, ABC):
    def make_sound(self):
        return "Woof!"
