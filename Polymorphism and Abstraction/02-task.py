from abc import ABC, abstractmethod
from math import pi


class Shapes(ABC):

    @abstractmethod
    def calculate_area(self):
        ...

    @abstractmethod
    def calculate_perimeter(self):
        ...


class Circle(Shapes):
    def __init__(self, radius: int):
        self.__radius = radius

    def calculate_perimeter(self):
        return 2 * pi * self.__radius

    def calculate_area(self):
        return pi * self.__radius ** 2


class Rectangle(Shapes):
    def __init__(self, height: int, width: int):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__height + self.__width)


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
