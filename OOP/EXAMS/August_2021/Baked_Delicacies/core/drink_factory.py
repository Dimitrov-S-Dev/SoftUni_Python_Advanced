from OOP.EXAMS.August_2021.Baked_Delicacies.drink.tea import Tea
from OOP.EXAMS.August_2021.Baked_Delicacies.drink.water import Water


class DrinkFactory:
    drink_types = {
        "Tea": Tea,
        "Water": Water,
    }

    def create_drink(self, drink_type: str, name: str, portion: int, brand: str):
        return self.drink_types[drink_type](name, portion, brand)

