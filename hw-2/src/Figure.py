from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("The argument must be an instance of Figure")
        return self.area() + figure.area()
