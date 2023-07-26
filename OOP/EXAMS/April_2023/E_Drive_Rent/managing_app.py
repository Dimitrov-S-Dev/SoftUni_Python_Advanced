from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLE = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan,
    }

    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    @property
    def get_road_id(self):
        return len(self.routes) + 1

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):

        if driving_license_number in [user.driving_license_number for user in self.users]:
            return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name, last_name,driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):

        if vehicle_type not in self.VALID_VEHICLE:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if license_plate_number in [vehicle.license_plate_number for vehicle in self.vehicles]:
            return f"{license_plate_number} belongs to another vehicle."

        vehicle = self.VALID_VEHICLE[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):

        curr_route = self.__find_route_by_st_point_end_point(start_point, end_point)
        if curr_route:
            if curr_route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            elif curr_route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            else:
                curr_route.is_locked = True

        r = Route(start_point, end_point, length, self.get_road_id)
        self.routes.append(r)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):

        user = [u for u in self.users if u.driving_license_number == driving_license_number][0]
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        route = [r for r in self.routes if r.route_id == route_id][0]
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        mileage = route.length
        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        vehicle.drive(mileage)
        return str(vehicle)

    def repair_vehicles(self, count: int):
        try:
            repair_vehicles = list(filter(lambda v: v.is_damaged, sorted(self.vehicles, key=lambda v: (v.brand, v.model))))[0:count]
        except IndexError:
            return
        for vehicle in repair_vehicles:
            vehicle.is_damaged = False
            vehicle.recharge()

        return f"{len(repair_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        users = sorted(self.users, key=lambda u: u.rating, reverse=True)
        output = f"*** E-Drive-Rent ***\n"
        for user in users:
            output += str(user) + "\n"

        return output.strip()

    def __find_route_by_st_point_end_point(self, start_point, end_point):
        try:
            route = next(filter(lambda r: r.start_point == start_point and r.end_point == end_point, self.routes))
            return route
        except StopIteration:
            return None



app = ManagingApp()
print(app.register_user( 'Tisha', 'Reenie', '7246506' ))
print(app.register_user( 'Bernard', 'Remy', 'CDYHVSR68661'))
print(app.register_user( 'Mack', 'Cindi', '7246506'))
print(app.upload_vehicle('PassengerCar', 'Chevrolet', 'Volt', 'CWP8032'))
print(app.upload_vehicle( 'PassengerCar', 'Volkswagen', 'e-Up!', 'COUN199728'))
print(app.upload_vehicle('PassengerCar', 'Mercedes-Benz', 'EQS', '5UNM315'))
print(app.upload_vehicle('CargoVan', 'Ford', 'e-Transit', '726QOA'))
print(app.upload_vehicle('CargoVan', 'BrightDrop', 'Zevo400', 'SC39690'))
print(app.upload_vehicle('EcoTruck', 'Mercedes-Benz', 'eActros', 'SC39690'))
print(app.upload_vehicle('PassengerCar', 'Tesla', 'CyberTruck', '726QOA'))
print(app.allow_route('SOF', 'PLD', 144))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('SOF', 'PLD', 184))
print(app.allow_route('BUR', 'VAR', 86.999))
print(app.make_trip('CDYHVSR68661', '5UNM315', 3, False))
print(app.make_trip('7246506', 'CWP8032', 1, True))
print(app.make_trip('7246506', 'COUN199728', 1, False))
print(app.make_trip('CDYHVSR68661', 'CWP8032', 3, False))
print(app.make_trip('CDYHVSR68661', '5UNM315', 2, False))
print(app.repair_vehicles(2))
print(app.repair_vehicles(20))
print(app.users_report())
