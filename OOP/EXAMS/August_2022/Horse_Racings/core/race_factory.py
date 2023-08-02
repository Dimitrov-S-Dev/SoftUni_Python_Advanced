from project.horse_race import HorseRace


class RaceFactory:
    @staticmethod
    def create_race(race_type):
        return HorseRace(race_type)
