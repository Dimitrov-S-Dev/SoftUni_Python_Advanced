from OOP.EXAMS.December_2022.Christmas_Pastry_Shop.delicacies.gingerbread import Gingerbread
from OOP.EXAMS.December_2022.Christmas_Pastry_Shop.delicacies.stolen import Stolen


class DelicacyFactory:
    VALID_TYPES = {"Gingerbread": Gingerbread, "Stolen": Stolen}

    def create_delicacy(self, type_delicacy, name, price):
        if type_delicacy not in self.VALID_TYPES:
            raise ValueError(f"{type_delicacy} is not on our delicacy menu!")
        return self.VALID_TYPES[type_delicacy](name, price)
