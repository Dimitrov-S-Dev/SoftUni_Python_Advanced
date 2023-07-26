from OOP.EXAMS.Re_Take_April_2023.E_Drive_Rent.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, self.MAX_MILEAGE)

    def drive(self, mileage: float):
        self.battery_level -= round(mileage / self.MAX_MILEAGE * 100)


