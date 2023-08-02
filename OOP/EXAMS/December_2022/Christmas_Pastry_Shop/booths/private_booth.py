from OOP.EXAMS.December_2022.Christmas_Pastry_Shop.booths.booth import Booth


class PrivateBooth(Booth):
    PPP_TO_RESERVE = 3.50

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        self.price_for_reservation = number_of_people * self.PPP_TO_RESERVE
        self.is_reserved = True
