from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        ...

    @abstractmethod
    def refuel(self, fuel):
        ...


class Car(Vehicle):
    AC_FUEL_CONS = 0.9

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self.AC_FUEL_CONS)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= (self.fuel_consumption + 0.9) * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AC_FUEL_CONS = 1.6

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self.AC_FUEL_CONS)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= (self.fuel_consumption + 1.6) * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95

