from project.animals.animal import Mammal


class Mouse(Mammal):
    @property
    def weight_incremental(self):
        return 0.1

    @property
    def food_eating(self):
        return ["Vegetable", "Fruit"]

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    @property
    def weight_incremental(self):
        return 0.4

    @property
    def food_eating(self):
        return ["Meat"]

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    @property
    def weight_incremental(self):
        return 0.3

    @property
    def food_eating(self):
        return ["Vegetable", "Meat"]

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    @property
    def weight_incremental(self):
        return 1

    @property
    def food_eating(self):
        return ["Meat"]

    def make_sound(self):
        return "ROAR!!!"
