from OOP.EXAMS.December_2022_Retake.Concert_Tracker_App.band import Band


class BandFactory:
    @staticmethod
    def create_band(name):
        return Band(name)
