# Think of it like this:

# ABC = "You MUST inherit from me, and I'll check at creation time."
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass

class Circle(Shape):  # must inherit
    def area(self): return 3.14

c = Circle()  # works
c2 = Shape()  # ERROR - can't instantiate abstract class directly
# If a child class forgets to implement `area()`, Python blocks you from creating the object — instant error.


# Protocol = "I don't care if you inherit from me. If your object has the right methods, you're good."


from typing import Protocol

class Flyer(Protocol):
    def fly(self) -> str: ...

class Bird:
    def fly(self) -> str:
        return "Bird flying"

class Airplane:
    def fly(self) -> str:
        return "Airplane flying"

class Fish:
    def swim(self) -> str:
        return "Fish swimming"

# Now any class with a fly() method is considered a Flyer:
def make_it_fly(thing: Flyer) -> None:
    print(thing.fly())

make_it_fly(Bird())      # works - has fly()
make_it_fly(Airplane())  # works - has fly()
make_it_fly(Fish())      # type-checker (mypy) flags error - no fly() method
                          # but Python itself won't stop you at runtime

# Neither `Bird` nor `Airplane` inherit from `Flyer` — they just happen to have a matching `fly()` method. That's the whole point of Protocol: structural typing, not inheritance-based.