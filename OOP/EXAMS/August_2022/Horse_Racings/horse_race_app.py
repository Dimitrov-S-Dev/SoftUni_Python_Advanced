from project.core.horse_factory import HorseFactory
from project.core.jockey_factory import JockeyFactory
from project.core.race_factory import RaceFactory


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []
        # first_upload

        self.horse_factory = HorseFactory()
        self.jockey_factory = JockeyFactory()
        self.race_factory = RaceFactory()

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):

        if self.__find_horse_by_name(horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")
        try:

            horse = self.horse_factory.create_horse(horse_type, horse_name, horse_speed)
        except ValueError:
            return
        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):

        if self.__find_jockey_by_name(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = self.jockey_factory.create_jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):

        if self.__find_race_by_type(race_type):
            raise Exception(f"Race {race_type} has been already created!")

        race = self.race_factory.create_race(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."
        # second_upload

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):

        jockey = self.__find_jockey_by_name(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        try:
            horse = list(filter(lambda h: h.__class__.__name__ == horse_type and not h.is_taken, self.horses))[-1]
        except IndexError:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):

        race = self.__find_race_by_type(race_type)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):

        race = self.__find_race_by_type(race_type)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        highest_speed = 0
        w_horse = None
        w_jockey = None
        for jockey in race.jockeys:
            if jockey.horse.speed > highest_speed:
                highest_speed = jockey.horse.speed
                w_horse = jockey.horse
                w_jockey = jockey

        return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is {w_jockey.name}! " \
               f"Winner's horse: {w_horse.name}."

    def __find_horse_by_name(self, name):
        for horse in self.horses:
            if horse.name == name:
                return horse
        return None

    def __find_jockey_by_name(self, name):
        for jockey in self.jockeys:
            if jockey.name == name:
                return jockey
        return None

    def __find_race_by_type(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
        return None

