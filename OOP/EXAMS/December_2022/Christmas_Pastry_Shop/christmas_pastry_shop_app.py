from OOP.EXAMS.December_2022.Christmas_Pastry_Shop.core.booth_factrory import BoothFactory
from OOP.EXAMS.December_2022.Christmas_Pastry_Shop.core.delicacy_factory import DelicacyFactory


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

        self.delicacy_factory = DelicacyFactory()
        self.booth_factory = BoothFactory()

    def add_delicacy(self, type_delicacy: str, name: str, price: float):

        if self.__find_delicacy_by_name(name):
            raise Exception(f"{name} already exists!")

        try:
            delicacy = self.delicacy_factory.create_delicacy(type_delicacy, name, price)
            self.delicacies.append(delicacy)
            return f"Added delicacy {name} - {type_delicacy} to the pastry shop."
        except ValueError as error:
            raise Exception(error)

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):

        if self.__find_booth_by_number(booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")

        try:
            booth = self.booth_factory.create_booth(type_booth, booth_number, capacity)
            self.booths.append(booth)
            return f"Added booth number {booth_number} in the pastry shop."
        except ValueError as error:
            raise Exception(error)

    def reserve_booth(self, number_of_people: int):

        try:
            booth = next(filter(lambda b: b.capacity >= number_of_people and not b.is_reserved, self.booths))
            booth.reserve(number_of_people)
            return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        except StopIteration:
            raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):

        booth = self.__find_booth_by_number(booth_number)
        if booth is None:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = self.__find_delicacy_by_name(delicacy_name)
        if delicacy is None:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth.booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.__find_booth_by_number(booth_number)
        self.income += booth.income()
        return booth.leave()

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    def __find_delicacy_by_name(self, name):
        for delicacy in self.delicacies:
            if delicacy.name == name:
                return delicacy
        return None

    def __find_booth_by_number(self, number):
        for booth in self.booths:
            if booth.booth_number == number:
                return booth
        return None
