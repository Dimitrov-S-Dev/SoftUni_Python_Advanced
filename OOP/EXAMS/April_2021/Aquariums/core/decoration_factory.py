from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class DecorationFactory:
    VALID_TYPES = {"Ornament": Ornament, "Plant": Plant}

    def create_decoration(self, decoration_type):
        return self.VALID_TYPES[decoration_type]()
