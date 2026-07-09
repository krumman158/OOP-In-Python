# Namespace = a container that holds a mapping of names (variables/functions/classes) to objects — prevents naming conflicts by keeping names scoped separately.


x = 10  # global namespace

def func():
    x = 20  # local namespace
    print(x)  # 20

func()
print(x)  # 10 (unaffected by local namespace)


# Types of namespaces:
# Local — inside a function
# Global — inside a module/file
# Built-in — Python's predefined names (`print`, `len`, etc.)
# Class/Instance — attributes/methods inside a class or object


class Dog:
    species = "Canine"  # class namespace

d = Dog()
d.name = "Bruno"  # instance namespace

print(Dog.species)  # Canine
print(d.name)        # Bruno