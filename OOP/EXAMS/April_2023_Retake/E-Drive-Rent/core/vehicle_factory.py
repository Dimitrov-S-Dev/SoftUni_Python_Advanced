from OOP.EXAMS.Re_Take_April_2023.E_Drive_Rent.vehicles.cargo_van import CargoVan
from OOP.EXAMS.Re_Take_April_2023.E_Drive_Rent.vehicles.passenger_car import PassengerCar


class VehicleFactory:
    VALID_TYPES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def create_vehicle(self, vehicle_type, brand, model, license_plate_number):
        if vehicle_type not in self.VALID_TYPES:
            raise ValueError(f"Vehicle type {vehicle_type} is inaccessible.")
        return self.VALID_TYPES[vehicle_type](brand, model, license_plate_number)
