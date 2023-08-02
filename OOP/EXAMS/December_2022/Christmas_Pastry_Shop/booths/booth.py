from abc import ABC, abstractmethod

from OOP.EXAMS.December_2022.Christmas_Pastry_Shop.core.validator import Validator


class Booth(ABC):
    def __init__(self, booth_number: int,  capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders = []
        self.price_for_reservation = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validator.raise_if_lt_zero(
            value,
            "Capacity cannot be a negative number!")
        self.__capacity = value

    @abstractmethod
    def reserve(self, number_of_people: int):
        pass

    def leave(self):
        bill = self.price_for_reservation + sum(d.price for d in self.delicacy_orders)
        self.price_for_reservation = 0
        self.is_reserved = False
        self.delicacy_orders = []
        return f"Booth {self.booth_number}:\n" + f"Bill: {bill:.2f}lv."

    def income(self):
        return self.price_for_reservation + sum(d.price for d in self.delicacy_orders)




