from OOP.EXAMS.August_2021.Baked_Delicacies.core.drink_factory import DrinkFactory
from OOP.EXAMS.August_2021.Baked_Delicacies.core.food_factory import FoodFactory
from OOP.EXAMS.August_2021.Baked_Delicacies.core.table_factory import TableFactory
from OOP.EXAMS.August_2021.Baked_Delicacies.core.validator import Validator


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

        self.food_factory = FoodFactory()
        self.drink_factory = DrinkFactory()
        self.table_factory = TableFactory()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty_or_white_space(
            value,
            f"Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):

        if any(f.name == name for f in self.food_menu):
            raise Exception(f"{food_type} {name} is already in the menu!")

        food = self.food_factory.create_food(food_type, name, price)
        self.food_menu.append(food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):

        if any(d.name == name for d in self.drinks_menu):
            raise Exception(f"{drink_type} {name} is already in the menu!")

        drink = self.drink_factory.create_drink(drink_type, name, portion, brand)
        self.drinks_menu.append(drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):

        if any(t.table_number == table_number for t in self.tables_repository):
            raise Exception(f"Table {table_number} is already in the bakery!")

        table = self.table_factory.create_table(table_type, table_number, capacity)
        self.tables_repository.append(table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):

        for table in self.tables_repository:
            if table.is_reserved:
                continue
            if table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names: str):

        if not self.__check_for_table_by_table_number(table_number):
            return f"Could not find table {table_number}"

        table = self.__find_table_by_table_number(table_number)

        ordered_foods = f"Table {table.table_number} ordered:\n"
        skipped_foods = f"{self.name} does not have in the menu:\n"
        for food_name in food_names:
            if self.__check_for_food_by_name(food_name):
                f = self.__find_food_by_name(food_name)
                table.order_food(f)
                ordered_foods += f"{repr(f)}\n"
            else:
                skipped_foods += food_name + "\n"

        return ordered_foods.strip() + "\n" + skipped_foods.strip()

    def order_drink(self, table_number: int, *drink_names: str):

        if not self.__check_for_table_by_table_number(table_number):
            return f"Could not find table {table_number}"

        table = self.__find_table_by_table_number(table_number)

        ordered_drinks = f"Table {table.table_number} ordered:\n"
        skipped_drinks = f"{self.name} does not have in the menu:\n"
        for drink_name in drink_names:
            if self.__check_for_drink_by_name(drink_name):
                d = self.__find_drink_by_name(drink_name)
                table.order_drink(d)
                ordered_drinks += f"{repr(d)}\n"
            else:
                skipped_drinks += drink_name + "\n"

        return ordered_drinks.strip() + "\n" + skipped_drinks.strip()

    def leave_table(self, table_number: int):

        table = self.__find_table_by_table_number(table_number)
        table_bill = table.get_bill()
        self.total_income += table_bill
        table.clear()
        return f"Table: {table.table_number}\nBill: {table_bill:.2f}"

    def get_free_tables_info(self):
        free_tables = [t for t in self.tables_repository if not t.is_reserved]
        output = ""
        for table in free_tables:
            output += table.free_table_info() + "\n"

        return output.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    def __check_for_food_by_name(self, food_name):
        for food in self.food_menu:
            if food.name == food_name:
                return True
        return None

    def __check_for_drink_by_name(self, drink_name):
        for drink in self.drinks_menu:
            if drink.name == drink_name:
                return True
        return None

    def __check_for_table_by_table_number(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return True
        return None

    def __find_food_by_name(self, food_name):
        for food in self.food_menu:
            if food.name == food_name:
                return food

    def __find_drink_by_name(self, drink_name):
        for drink in self.drinks_menu:
            if drink.name == drink_name:
                return drink

    def __find_table_by_table_number(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table
