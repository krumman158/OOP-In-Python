#                     Abstract Methods

# these method's definition is implemented in base class.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area())  # user just calls area(), doesn't need to know the formula's internal logic