from OOP.Exam_Prep.Feb_2023.Part_1.Christmas_Pastry_Shop.booths.booth import \
    Booth


class PrivateBooth(Booth):

    @property
    def get_ppp(self):
        return 3.50

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        self.is_reserved = True
        self.price_for_reservation = number_of_people * self.get_ppp
