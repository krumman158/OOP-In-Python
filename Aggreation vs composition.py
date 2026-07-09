# Composition: a class contains objects of other classes as attributes to build functionality (a "has-a" relationship), and the contained object's lifecycle depends on the container.

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car "has-a" Engine
    def start(self):
        self.engine.start()

c = Car()
c.start()

# Aggregation vs Composition:
# - Aggregation: "has-a" relationship, but contained object can exist independently (weaker link).
# - Composition: "has-a" relationship, but contained object cannot exist without the container (stronger link).


# Aggregation
class Teacher:
    pass
class Department:
    def __init__(self, teacher):
        self.teacher = teacher  # Teacher exists independently

teacher = Teacher()
dept = Department(teacher)  # Teacher can exist even if Department is deleted

# Composition over Inheritance: a design principle — prefer building classes using composition (has-a) instead of inheritance (is-a), because it's more flexible, avoids deep/rigid class hierarchies, and reduces tight coupling.