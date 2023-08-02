from OOP.EXAMS.August_2022.Horse_Racings.jockey import Jockey


class JockeyFactory:
    @staticmethod
    def create_jockey(name, age):
        return Jockey(name, age)
