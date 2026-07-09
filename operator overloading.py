#                                         Operator Overloading

# Operator overloading = defining custom behavior for operators (`+`, `-`, `==`, etc.) for objects of a class, using special/dunder methods (e.g., `__add__`, `__eq__`).

# 1) Arithmetic:
class Point:
    def __init__(self, x):
        self.x = x
    def __add__(self, other):
        return Point(self.x + other.x)
    def __sub__(self, other):
        return Point(self.x - other.x)
    def __mul__(self, other):
        return Point(self.x * other.x)
    def __floordiv__(self, other):
        return Point(self.x // other.x)
    def __truediv__(self, other):
        return Point(self.x / other.x)


# 2) Comparison:

    def __eq__(self, other):
        return self.x == other.x
    def __lt__(self, other):
        return self.x < other.x
    def __gt__(self, other):
        return self.x > other.x
    def __ge__(self, other):
        return self.x >= other.x
    def __le__(self, other):
        return self.x <= other.x


# 3) Unary:
    def __neg__(self):
        return Point(-self.x)


# 4) Length:

    def __len__(self):
        return self.x
    
# 5) get item
    def __getitem__(self, index):
        return self.x[index]


# __str__ → readable/user-friendly string (used by print(), str())
# __repr__→ unambiguous/developer-focused string (used in debugging, repr(), shown in console/REPL)

class Point:
    def __init__(self, x):
        self.x = x
    def __str__(self):
        return f"Point at {self.x}"
    def __repr__(self):
        return f"Point({self.x})"

p = Point(5)
print(p)      # Point at 5   (__str__)
print(repr(p))# Point(5)     (__repr__)

# If `__str__` isn't defined, Python falls back to `__repr__`.

# __hash__

# Hash = a fixed-size integer generated from an object's value, used to quickly compare/lookup objects in sets and dictionaries. For this objects must be immutable
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

p1 = Point(2, 3)
p2 = Point(2, 3)

print(p1 == p2)        # True
print(hash(p1) == hash(p2))  # True

s = {p1, p2}
print(len(s))           # 1 (treated as same object since equal + same hash)

# '__eq__ → defines how two objects are compared for equality (==). By default (dataclass), compares all fields.
# __hash__ → returns an integer hash value for the object, used in sets/dicts as keys. Objects with __eq__ defined are normally unhashable (__hash__ set to None) unless you make them immutable (frozen=True in dataclass) or manually define __hash__.


