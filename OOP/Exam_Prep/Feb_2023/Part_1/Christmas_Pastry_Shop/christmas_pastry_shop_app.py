from typing import List

from OOP.Exam_Prep.Feb_2023.Part_1.Christmas_Pastry_Shop.booths.booth import \
    Booth
from OOP.Exam_Prep.Feb_2023.Part_1.Christmas_Pastry_Shop.booths.open_booth import \
    OpenBooth
from OOP.Exam_Prep.Feb_2023.Part_1.Christmas_Pastry_Shop.booths.private_booth import \
    PrivateBooth
from OOP.Exam_Prep.Feb_2023.Part_1.Christmas_Pastry_Shop.delicacies.delicacy import \
    Delicacy
from OOP.Exam_Prep.Feb_2023.Part_1.Christmas_Pastry_Shop.delicacies.gingerbread import \
    Gingerbread
from OOP.Exam_Prep.Feb_2023.Part_1.Christmas_Pastry_Shop.delicacies.stolen import \
    Stolen


class ChristmasPastryShopApp:
    VALID_DELICACIES = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen,
    }

    VALID_BOOTH = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth,
    }

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        delicacy = [d for d in self.delicacies if d.name == name]

        if delicacy:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.VALID_DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = self.VALID_DELICACIES[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        booth = [b for b in self.booths if b.booth_number == booth_number]

        if booth:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.VALID_BOOTH:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = self.VALID_BOOTH[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for " \
                       f"{number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        delicacy = [d for d in self.delicacies if d.name == delicacy_name]

        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth = [b for b in self.booths if b.booth_number == booth_number]

        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        booth[0].delicacy_orders.append(delicacy[0])
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = [b for b in self.booths if b.booth_number == booth_number][0]
        bill = booth.price_for_reservation + sum(d.price for d in booth.delicacy_orders)

        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0

        self.income += bill
        return f"Booth {booth.booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
