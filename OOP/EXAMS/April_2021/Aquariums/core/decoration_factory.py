from OOP.EXAMS.April_2021.Aquariums.decoration.ornament import Ornament
from OOP.EXAMS.April_2021.Aquariums.decoration.plant import Plant


class DecorationFactory:
    VALID_TYPES = {"Ornament": Ornament, "Plant": Plant}

    def create_decoration(self, decoration_type):
        return self.VALID_TYPES[decoration_type]()
