from OOP.EXAMS.August_2021_Retake.Spase_Station.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut
        return None

    def recharge_by_ten(self):
        for astronaut in self.astronauts:
            astronaut.increase_oxygen(10)

    def filter_by_oxygen_units(self, units=30):
        return sorted(filter(lambda a: a.oxygen > units, self.astronauts), key=lambda a: -a.oxygen)[:5]
