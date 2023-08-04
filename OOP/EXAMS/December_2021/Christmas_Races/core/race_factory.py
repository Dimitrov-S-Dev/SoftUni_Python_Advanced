from OOP.EXAMS.December_2021.Christmas_Races.race import Race


class RaceFactory:

    @staticmethod
    def create_race(name):
        return Race(name)
