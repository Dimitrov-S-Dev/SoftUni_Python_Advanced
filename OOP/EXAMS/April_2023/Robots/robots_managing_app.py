from OOP.EXAMS.April_2023.Robots.robots.female_robot import FemaleRobot
from OOP.EXAMS.April_2023.Robots.robots.male_robot import MaleRobot
from OOP.EXAMS.April_2023.Robots.services.main_service import MainService
from OOP.EXAMS.April_2023.Robots.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE = {
        "MainService": MainService,
        "SecondaryService": SecondaryService,
    }

    VALID_ROBOTS = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot,
    }

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):

        if service_type not in self.VALID_SERVICE:
            raise Exception("Invalid service type!")

        service = self.VALID_SERVICE[service_type](name)
        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):

        if robot_type not in self.VALID_ROBOTS:
            raise Exception("Invalid robot type!")

        robot = self.VALID_ROBOTS[robot_type](name, kind, price)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.__find_robot_by_name(robot_name)
        service = self.__find_service_by_name(service_name)

        robot_type = self.__find_robot_type_by_name(robot_name)
        service_type = self.__find_service_type_by_name(service_name)

        if self.__find_robot_type_service_type_miss_match(robot_type, service_type):
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception(f"Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):

        service = self.__find_service_by_name(service_name)
        if robot_name not in [r.name for r in service.robots]:
            raise Exception("No such robot in this service!")

        robot = [r for r in service.robots if r.name == robot_name][0]
        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.__find_service_by_name(service_name)
        for robot in service.robots:
            robot.eating()
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self.__find_service_by_name(service_name)
        total_price = sum(r.price for r in service.robots)

        return f"The value of service {service.name} is {total_price:.2f}."

    def __str__(self):
        output = ""
        for service in self.services:
            output += service.details() + "\n"

        return output.strip()

    def __find_robot_by_name(self, robot_name):
        return [r for r in self.robots if r.name == robot_name][0]

    def __find_service_by_name(self, service_name):
        return [s for s in self.services if s.name == service_name][0]

    def __find_robot_type_by_name(self, name):
        for robot in self.robots:
            if robot.name == name:
                return robot.__class__.__name__

    def __find_service_type_by_name(self, name):
        for service in self.services:
            if service.name == name:
                return service.__class__.__name__

    @staticmethod
    def __find_robot_type_service_type_miss_match(robot_type, service_type):
        if robot_type == "FemaleRobot" and service_type == "MainService":
            return True
        elif robot_type == "MaleRobot" and service_type == "SecondaryService":
            return True

