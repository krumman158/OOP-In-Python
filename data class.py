# @dataclass = a decorator that auto-generates boilerplate code (__init__, __repr__, __eq__) for classes mainly used to store data.

# In it-:-
#  order=True → auto-generates comparison methods (`__lt__`, `__le__`, `__gt__`, `__ge__`) so objects can be compared/sorted based on field values.

# frozen=True → makes the object immutable (can't change attributes after creation) — trying to modify raises an error. Also allows the object to be hashable (`__hash__`).

from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Point:
    x: int
    y: int

p1 = Point(2, 3)
p2 = Point(2, 4)

print(p1)              # __repr__  -> Point(x=2, y=3, tags=[])
print(p1 == p2)         # __eq__    -> False
print(p1 < p2)          # __lt__    -> True (order=True)
print(p1 <= p2)         # __le__    -> True
print(p1 > p2)          # __gt__    -> False
print(p1 >= p2)         # __ge__    -> False
print(hash(p1))         # __hash__  -> works because frozen=True

# - `order=True` → adds `__lt__`, `__le__`, `__gt__`, `__ge__`
# - `frozen=True` → makes object immutable + adds `__hash__`