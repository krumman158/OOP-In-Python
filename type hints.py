# Type hints = annotations that specify expected data types for variables, attributes, and function parameters/return values (not enforced at runtime, just for readability/tooling).

class Point:
    x: int          # attribute type hint
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def distance(self, other: "Point") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

p1 = Point(0, 0)
p2 = Point(3, 4)
print(p1.distance(p2))  # 5.0


# x: int → hints attribute type
# other: "Point" → hints parameter type
# -> float → hints return type