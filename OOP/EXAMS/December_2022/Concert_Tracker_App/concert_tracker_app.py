from OOP.EXAMS.December_2022.Concert_Tracker_App.core.band_factory import BandFactory
from OOP.EXAMS.December_2022.Concert_Tracker_App.core.concert_factory import ConcertFactory
from OOP.EXAMS.December_2022.Concert_Tracker_App.core.musician_factory import MusicianFactory


class ConcertTrackerApp:
    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

        self.musician_factory = MusicianFactory()
        self.band_factory = BandFactory()
        self.concert_factory = ConcertFactory()

    def create_musician(self, musician_type: str, name: str, age: int):

        try:
            musician = self.musician_factory.create_musician(musician_type, name, age)
        except ValueError as error:
            raise ValueError(error)

        if self.__find_musician_by_name(name):
            raise Exception(f"{name} is already a musician!")

        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, band_name: str):
        if self.__find_band_by_name(band_name):
            raise Exception(f"{band_name} band is already created!")

        band = self.band_factory.create_band(band_name)
        self.bands.append(band)
        return f"{band_name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):

        curr_concert = self.__find_concert_by_place(place)
        if curr_concert:
            raise Exception(f"{place} is already registered for {curr_concert.genre} concert!")

        concert = self.concert_factory.create_concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):

        musician = self.__find_musician_by_name(musician_name)
        if musician is None:
            raise Exception(f"{musician_name} isn't a musician!")

        band = self.__find_band_by_name(band_name)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        band.add_member(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.__find_band_by_name(band_name)
        if band is None:
            raise Exception(f"{band_name} isn't a band!")
        try:
            musician = next(filter(lambda m: m.name == musician_name, band.members))
            band.remove_member(musician)
            return f"{musician_name} was removed from {band_name}."
        except StopIteration:
            raise Exception(f"{musician_name} isn't a member of {band.name}!")

    def start_concert(self, concert_place: str, band_name: str):
        concert = self.__find_concert_by_place(concert_place)
        band = self.__find_band_by_name(band_name)

        members = set([m.__class__.__name__ for m in band.members])
        if len(members) < 3:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == "Rock":
            valid_skills = {"play the drums with drumsticks",
                            "sing high pitch notes",
                            "play rock"}
            members_skills = set([",".join(m.skills) for m in band.members])
            if not valid_skills.issubset(members_skills):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")
        elif concert.genre == "Metal":
            valid_skills = {"play the drums with drumsticks",
                            "sing low pitch notes",
                            "play metal"}
            members_skills = set([",".join(m.skills) for m in band.members])
            if not valid_skills.issubset(members_skills):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")
        elif concert.genre == "Jazz":
            valid_skills = {"play the drums with drum brushes",
                            "sing low pitch notes",
                            "sing high pitch notes",
                            "play jazz"}
            members_skills = set([",".join(m.skills) for m in band.members])
            if not valid_skills.issubset(members_skills):
                raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.profit()
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

    def __find_musician_by_name(self, name):
        for musician in self.musicians:
            if musician.name == name:
                return musician
        return None

    def __find_band_by_name(self, name):
        for band in self.bands:
            if band.name == name:
                return band
        return None

    def __find_concert_by_place(self, place):
        for concert in self.concerts:
            if concert.place == place:
                return concert
