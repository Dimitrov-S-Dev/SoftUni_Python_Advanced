from OOP.EXAMS.August_2022.Horse_Racings.horse_specification.appaloosa import Appaloosa
from OOP.EXAMS.August_2022.Horse_Racings.horse_specification.thoroughbred import Thoroughbred


class HorseFactory:
    VALID_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def create_horse(self, horse_type, name, speed):
        if horse_type not in self.VALID_TYPES:
            raise ValueError("not valid")
        return self.VALID_TYPES[horse_type](name, speed)
    