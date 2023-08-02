from OOP.EXAMS.December_2022_Retake.Concert_Tracker_App.band_members.musician import Musician


class Singer(Musician):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        
    @property
    def skills_available(self):
        return ["sing high pitch notes",
                "sing low pitch notes"]
    