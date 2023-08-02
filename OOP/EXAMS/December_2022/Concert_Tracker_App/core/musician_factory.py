from OOP.EXAMS.December_2022.Concert_Tracker_App.band_members.drummer import Drummer
from OOP.EXAMS.December_2022.Concert_Tracker_App.band_members.guitarist import Guitarist
from OOP.EXAMS.December_2022.Concert_Tracker_App.band_members.singer import Singer


class MusicianFactory:
    VALID_TYPES = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def create_musician(self, musician_type, name, age):
        if musician_type not in self.VALID_TYPES:
            raise ValueError("Invalid musician type!")
        return self.VALID_TYPES[musician_type](name, age)
