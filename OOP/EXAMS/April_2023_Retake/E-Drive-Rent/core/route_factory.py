from OOP.EXAMS.Re_Take_April_2023.E_Drive_Rent.route import Route


class RouteFactory:
    @staticmethod
    def create_route(start_point, end_point, length, route_id):
        return Route(start_point, end_point, length, route_id)
