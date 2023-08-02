from OOP.EXAMS.December_2022.Christmas_Pastry_Shop.booths.open_booth import OpenBooth
from OOP.EXAMS.December_2022.Christmas_Pastry_Shop.booths.private_booth import PrivateBooth


class BoothFactory:
    VALID_TYPES = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def create_booth(self, booth_type, booth_number, capacity):
        if booth_type not in self.VALID_TYPES:
            raise ValueError(f"{booth_type} is not a valid booth!")
        return self.VALID_TYPES[booth_type](booth_number, capacity)
