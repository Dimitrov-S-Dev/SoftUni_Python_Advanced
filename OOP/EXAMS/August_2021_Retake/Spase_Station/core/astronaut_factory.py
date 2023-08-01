from OOP.EXAMS.August_2021_Retake.Spase_Station.astronaut.biologist import Biologist
from OOP.EXAMS.August_2021_Retake.Spase_Station.astronaut.geodesist import Geodesist
from OOP.EXAMS.August_2021_Retake.Spase_Station.astronaut.meteorologist import Meteorologist


class AstronautFactory:
    VALID_TYPES = {"Biologist": Biologist, "Geodesist": Geodesist, "Meteorologist": Meteorologist}

    def create_astronaut(self, astronaut_type, name):
        if astronaut_type not in self.VALID_TYPES:
            raise ValueError("Astronaut type is not valid!")
        return self.VALID_TYPES[astronaut_type](name)
