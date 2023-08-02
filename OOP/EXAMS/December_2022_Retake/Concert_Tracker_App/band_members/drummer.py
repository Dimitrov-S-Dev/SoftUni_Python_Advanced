from OOP.EXAMS.December_2022_Retake.Concert_Tracker_App.band_members.musician import Musician


class Drummer(Musician):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    @property
    def skills_available(self):
        return ["play the drums with drumsticks",
                "play the drums with drum brushes",
                "read sheet music"]
