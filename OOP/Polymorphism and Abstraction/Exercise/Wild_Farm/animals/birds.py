from project.animals.animal import Bird


class Owl(Bird):
    @property
    def weight_incremental(self):
        return 0.25

    @property
    def food_eating(self):
        return ["Meat"]

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    @property
    def weight_incremental(self):
        return 0.35

    @property
    def food_eating(self):
        return ["Meat", "Vegetable", "Fruit", "Seed"]

    def make_sound(self):
        return "Cluck"

