from OOP.EXAMS.August_2022.Horse_Racings.horse_race import HorseRace


class RaceFactory:
    @staticmethod
    def create_race(race_type):
        return HorseRace(race_type)
