from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area_calculate(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_calculate(self):
        return self.width * self.height


class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    @property
    def shapes(self):
        return self.__shapes
    
    @shapes.setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise AssertionError("Shapes should be of type 'list'.")

        self.__shapes = value

    @property
    def total_area(self):
        total = 0

        for shape in self.shapes:
            total += shape.area_calculate()

        return total


shapes = [Rectangle(2, 3), Rectangle(1, 6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
