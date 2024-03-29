from abc import ABC, abstractmethod
from OOP.EXAMS.April_2023_Retake.E_Drive_Rent.core.validator import Validator


class BaseVehicle(ABC):
    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage: float):
        self.brand = brand
        self.model = model
        self.license_plate_number = license_plate_number
        self.max_mileage = max_mileage
        self.battery_level = 100
        self.is_damaged = False

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        Validator.raise_if_empty_string_or_w_space(
            value,
            "Brand cannot be empty!")
        self.__brand = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        Validator.raise_if_empty_string_or_w_space(
            value, 
            "Model cannot be empty!")
        self.__model = value
        
    @property
    def license_plate_number(self):
        return self.__license_plate_number
    
    @license_plate_number.setter
    def license_plate_number(self, value):
        Validator.raise_if_empty_string_or_w_space(
            value,
            "License plate number is required!")
        self.__license_plate_number = value

    @abstractmethod
    def drive(self, mileage: float):
        pass

    def recharge(self):
        self.battery_level = 100

    def change_status(self):
        self.is_damaged = not self.is_damaged

    def __str__(self):
        return f"{self.brand} {self.model} License plate: {self.license_plate_number} Battery: {self.battery_level}% " \
               f"Status: {'OK' if not self.is_damaged else 'Damaged'}"
