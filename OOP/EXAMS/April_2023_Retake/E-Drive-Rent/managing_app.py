

class ManagingApp:
    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

        self.user_factory = UserFactory()
        self.vehicle_factory = VehicleFactory()
        self.route_factory = RouteFactory()

    @property
    def route_id(self):
        return len(self.routes) + 1

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):

        if self.__find_user_by_driving_license(driving_license_number):
            return f"{driving_license_number} has already been registered to our platform."

        user = self.user_factory.create_user(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):

        try:
            vehicle = self.vehicle_factory.create_vehicle(vehicle_type, brand, model, license_plate_number)

        except ValueError as error:
            return f"{error}"

        if self.__find_vehicle_by_license_plate(license_plate_number):
            return f"{license_plate_number} belongs to another vehicle."

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

        route = self.route_factory.create_route(start_point, end_point, length, self.route_id)
        self.routes.append(route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened):

        curr_user = self.__find_user_by_driving_license(driving_license_number)
        curr_vehicle = self.__find_vehicle_by_license_plate(license_plate_number)
        curr_route = self.__find_route_by_route_id(route_id)

        if curr_user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if curr_vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if curr_route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        mileage = curr_route.length
        curr_vehicle.drive(mileage)
        if is_accident_happened:
            curr_vehicle.is_damaged = True
            curr_user.decrease_rating()
        else:
            curr_user.increase_rating()

        return str(curr_vehicle)

    def repair_vehicles(self, count: int):
        vehicles = self.__sort_vehicle_by_damage(count)
        if vehicles:
            for vehicle in vehicles:
                vehicle.is_damaged = False
                vehicle.recharge()
        return f"{len(vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        output = f"*** E-Drive-Rent ***" + "\n"
        for user in sorted(self.users, key=lambda u: -u.rating):
            output += str(user) + "\n"
        return output.strip()


    def __find_user_by_driving_license(self, driving_license_number):
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return user
        return None

    def __find_vehicle_by_license_plate(self, license_plate):
        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate:
                return vehicle
        return None

    def __find_route_by_route_id(self, route_id):
        for rout in self.routes:
            if rout.route_id == route_id:
                return rout
        return None

    def __find_route_by_st_point_end_point(self, start_point, end_point):
        try:
            route = next(filter(lambda r: r.start_point == start_point and r.end_point == end_point, self.routes))
            return route
        except StopIteration:
            return None

    def __sort_vehicle_by_damage(self, count):
        vehicles = sorted(filter(lambda v: v.is_damaged, self.vehicles), key=lambda v: (v.brand, v.model))[:count]
        return vehicles





