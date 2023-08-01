from project.astronaut.astronaut_repository import AstronautRepository
from project.core.astronaut_factory import AstronautFactory
from project.core.planet_factory import PlanetFactory
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

        self.astronaut_factory = AstronautFactory()
        self.planet_factory = PlanetFactory()
        self.successful_missions = 0
        self.not_complete_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        try:
            astronaut = self.astronaut_factory.create_astronaut(astronaut_type, name)
            self.astronaut_repository.add(astronaut)
            return f"Successfully added {astronaut_type}: {name}."
        except ValueError as error:
            raise Exception(error)

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet = self.planet_factory.create_planet(name, items)
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        self.astronaut_repository.recharge_by_ten()

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception("Invalid planet name!")

        astronauts = self.astronaut_repository.filter_by_oxygen_units()

        if len(astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        a_count = 0
        for astronaut_ in astronauts:
            if len(planet.items) == 0:
                break
            while len(planet.items) > 0 and astronaut_.oxygen > 0:
                item = planet.pick_item()
                astronaut_.add_item(item)
                astronaut_.breathe()
            a_count += 1

        if len(planet.items) > 0:
            self.not_complete_missions += 1
            return "Mission is not completed."

        self.successful_missions += 1
        return f"Planet: {planet.name} was explored. {a_count} astronauts participated in collecting items."

    def report(self):
        result = f"{self.successful_missions} successful missions!" + "\n"
        result += f"{self.not_complete_missions} missions were not completed!" + "\n"
        result += f"Astronauts' info:" + "\n"

        for a in self.astronaut_repository.astronauts:
            result += str(a) + "\n"
        return result.strip()
