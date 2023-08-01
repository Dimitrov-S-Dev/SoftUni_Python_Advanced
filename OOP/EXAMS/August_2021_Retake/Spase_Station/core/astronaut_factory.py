from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist


class AstronautFactory:
    VALID_TYPES = {"Biologist": Biologist, "Geodesist": Geodesist, "Meteorologist": Meteorologist}

    def create_astronaut(self, astronaut_type, name):
        if astronaut_type not in self.VALID_TYPES:
            raise ValueError("Astronaut type is not valid!")
        return self.VALID_TYPES[astronaut_type](name)
