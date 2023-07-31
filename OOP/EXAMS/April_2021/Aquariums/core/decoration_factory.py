from OOP.EXAMS.April_2021.Aquariums.decoration.ornament import Ornament
from OOP.EXAMS.April_2021.Aquariums.decoration.plant import Plant


class DecorationFactory:
    VALID_TYPES = {"Ornament": Ornament, "Plant": Plant}

    def create_decoration(self, decoration_type):
        if decoration_type not in self.VALID_TYPES:
            raise ValueError("Invalid decoration type.")
        return self.VALID_TYPES[decoration_type]()
