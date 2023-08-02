from OOP.EXAMS.April_2023_Retake.E_Drive_Rent.core.validator import Validator


class Route:
    def __init__(self, start_point: str, end_point: str, length: float, route_id: int):
        self.start_point = start_point
        self.end_point = end_point
        self.length = length
        self.route_id = route_id
        self.is_locked = False

    @property
    def start_point(self):
        return self.__start_point

    @start_point.setter
    def start_point(self, value):
        Validator.raise_if_empty_string_or_w_space(
            value,
            "Start point cannot be empty!")
        self.__start_point = value

    @property
    def end_point(self):
        return self.__end_point

    @end_point.setter
    def end_point(self, value):
        Validator.raise_if_empty_string_or_w_space(
            value,
            "End point cannot be empty!")
        self.__end_point = value

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        Validator.raise_if_value_is_lt_min_value(
            value,
            1.00,
            "Length cannot be less than 1.00 kilometer!")
        self.__length = value
