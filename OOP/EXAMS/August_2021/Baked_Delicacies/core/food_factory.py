from project.baked_food.bread import Bread
from project.baked_food.cake import Cake


class FoodFactory:
    food_types = {
        "Bread": Bread,
        "Cake": Cake,
    }

    def create_food(self, food_type: str, name: str, price: float):
        if food_type in self.food_types:
            return self.food_types[food_type](name, price)
