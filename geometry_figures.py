from abc import ABC, abstractmethod
from math import sqrt, pi


class Parameters:
    def __init__(self, size):
        self.size = size
        self.strategy = Circle()

    def choose_figure(self, new_strategy):
        self.strategy = new_strategy

    def area(self) -> float:
        return round(self.strategy.calculate_area(self.size), 2)

    def perimeter(self) -> float:
        return round(self.strategy.calculate_perimeter(self.size), 2)

    def volume(self) -> float:
        return round(self.strategy.calculate_volume(self.size), 2)


# Strategy interface
class CalculationStrategy(ABC):
    @abstractmethod
    def calculate_perimeter(self, size):
        pass

    @abstractmethod
    def calculate_area(self, size):
        pass

    @abstractmethod
    def calculate_volume(self, size):
        pass


# Concrete strategies
class Circle(CalculationStrategy):
    def calculate_perimeter(self, size):
        return 2 * pi * size

    def calculate_area(self, size):
        return pi * size**2

    def calculate_volume(self, *args):
        return 0


class Triangle(CalculationStrategy):
    def calculate_perimeter(self, size):
        return size * 3

    def calculate_area(self, size):
        return size**2 * sqrt(3) / 4

    def calculate_volume(self, *args):
        return 0


class Square(CalculationStrategy):
    def calculate_perimeter(self, size):
        return size * 4

    def calculate_area(self, size):
        return size**2

    def calculate_volume(self, *args):
        return 0


class Pentagon(CalculationStrategy):
    def calculate_perimeter(self, size):
        return size * 5

    def calculate_area(self, size):
        return size**2 / 4 * sqrt(25 + 10 * sqrt(5))

    def calculate_volume(self, *args):
        return 0


class Hexagon(CalculationStrategy):
    def calculate_perimeter(self, size):
        return size * 6

    def calculate_area(self, size):
        return 3 * size ** 2 * sqrt(3) / 2

    def calculate_volume(self, *args):
        return 0


class Cube(CalculationStrategy):
    def calculate_perimeter(self, size):
        return size * 12

    def calculate_area(self, size):
        return size**2 * 6

    def calculate_volume(self, size):
        return size**3


if __name__ == '__main__':
    figure = Parameters(10)

    figure.choose_figure(Circle())
    assert figure.area() == 314.16

    figure.choose_figure(Triangle())
    assert figure.perimeter() == 30

    figure.choose_figure(Square())
    assert figure.area() == 100

    figure.choose_figure(Pentagon())
    assert figure.perimeter() == 50

    figure.choose_figure(Hexagon())
    assert figure.perimeter() == 60

    figure.choose_figure(Cube())
    assert figure.volume() == 1000
