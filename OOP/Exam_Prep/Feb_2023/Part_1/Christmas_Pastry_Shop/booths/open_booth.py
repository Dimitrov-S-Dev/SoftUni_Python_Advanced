from project.booths.booth import Booth


class OpenBooth(Booth):

    @property
    def get_ppp(self):
        return 2.50

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        self.is_reserved = True
        self.price_for_reservation = number_of_people * self.get_ppp

