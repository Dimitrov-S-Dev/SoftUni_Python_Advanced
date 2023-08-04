from itertools import islice

from OOP.EXAMS.December_2021.Christmas_Races.core.car_factory import CarFactory
from OOP.EXAMS.December_2021.Christmas_Races.core.driver_factory import DriverFactory
from OOP.EXAMS.December_2021.Christmas_Races.core.race_factory import RaceFactory


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

        self.car_factory = CarFactory()
        self.driver_factory = DriverFactory()
        self.race_factory = RaceFactory()

    def create_car(self, car_type: str, model: str, speed_limit: int):

        if any(c.model == model for c in self.cars):
            raise Exception(f"Car {model} is already created!")

        if car_type not in ["MuscleCar", "SportsCar"]:
            return
        car = self.car_factory.create_car(car_type, model, speed_limit)
        self.cars.append(car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):

        if any(d.name == driver_name for d in self.drivers):
            raise Exception(f"Driver {driver_name} is already created!")

        driver = self.driver_factory.create_driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):

        if any(r.name == race_name for r in self.races):
            raise Exception(f"Race {race_name} is already created!")

        race = self.race_factory.create_race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):

        try:
            driver = next(filter(lambda d: d.name == driver_name, self.drivers))
        except StopIteration:
            raise Exception(f"Driver {driver_name} could not be found!")

        try:
            car = list(filter(lambda c: c.__class__.__name__ == car_type and not c.is_taken, self.cars))[-1]
        except IndexError:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car:
            old_model = driver.car.model
            driver.car.is_taken = False
            new_model = car.model
            driver.car = car
            car.is_taken = True
            return f"Driver {driver.name} changed his car from {old_model} to {new_model}."

        driver.car = car
        car.is_taken = True
        return f"Driver {driver.name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):

        try:
            race = next(filter(lambda r: r.name == race_name, self.races))
        except StopIteration:
            raise Exception(f"Race {race_name} could not be found!")

        try:
            driver = next(filter(lambda d: d.name == driver_name, self.drivers))
        except StopIteration:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):

        try:
            race = next(filter(lambda r: r.name == race_name, self.races))
        except StopIteration:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        result = {}

        for driver in race.drivers:
            curr_car_speed = driver.car.speed_limit
            result[driver] = curr_car_speed

        sorted_result = {item[0]: item[1] for item in sorted(result.items(), key=lambda item: -item[1])}
        first_three = dict(islice(sorted_result.items(), 3))
        for driver in first_three:
            driver.win()

        output = ""
        for driver, speed in first_three.items():
            output += f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.\n"

        return output.strip()
