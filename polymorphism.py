#                                                 Polymorphism

# Polymorphism = same method name behaves differently depending on the object/class calling it (one interface, multiple implementations).

# It has two key concepts i: method over riding and operator overloading

from typing import override

class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    @override
    def sound(self):
        print("Bark")

a=Animal()
a.sound()

d=Dog()
d.sound()