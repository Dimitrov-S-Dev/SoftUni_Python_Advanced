from abc import ABC, abstractmethod

from OOP.EXAMS.August_2021.Baked_Delicacies.baked_food.baked_food import BakedFood
from OOP.EXAMS.August_2021.Baked_Delicacies.core.validator import Validator
from OOP.EXAMS.August_2021.Baked_Delicacies.drink.drink import Drink


class Table(ABC):
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False
        self.food_not_on_menu = []
        self.drink_not_on_menu = []

    @property
    @abstractmethod
    def min_number(self):
        pass

    @property
    @abstractmethod
    def max_number(self):
        pass

    @property
    @abstractmethod
    def error_message(self):
        pass

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        Validator.raise_if_number_is_not_in_range(value, self.min_number(), self.max_number(), self.error_message())
        self.__table_number = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validator.raise_if_number_is_less_or_equal_to_zero(
            value,
            f"Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people: int):
        self.is_reserved = True
        self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        return sum(f.price for f in self.food_orders) + sum(d.price for d in self.drink_orders)

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\n"\
                   f"Type: {self.__class__.__name__}\n"\
                   f"Capacity: {self.capacity}"
