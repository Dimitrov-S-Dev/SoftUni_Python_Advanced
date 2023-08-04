from OOP.EXAMS.December_2021.Christmas_Races.car.muscle_car import MuscleCar
from OOP.EXAMS.December_2021.Christmas_Races.car.sports_car import SportsCar


class CarFactory:
    valid_cars = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar,
    }

    def create_car(self, car_type, model, speed_limit):
        return self.valid_cars[car_type](model, speed_limit)
