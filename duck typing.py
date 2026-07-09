
class Duck:
    def sound(self):
        return "Quack"

class Dog:
    def sound(self):
        return "Bark"

class Car:
    def sound(self):
        return "Vroom"

# if any object has sound() then it is a duck
def make_sound(thing):
    print(thing.sound())  # doesn't care what type "thing" is

make_sound(Duck())  # Quack
make_sound(Dog())   # Bark
make_sound(Car())   # Vroom


# "If it walks like a duck and quacks like a duck, it's a duck" — Python doesn't check the object's type, just whether it has the method being called (`sound()`).