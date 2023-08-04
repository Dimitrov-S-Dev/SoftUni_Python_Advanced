from OOP.EXAMS.December_2021.Christmas_Races.driver import Driver


class DriverFactory:

    @staticmethod
    def create_driver(name):
        return Driver(name)
