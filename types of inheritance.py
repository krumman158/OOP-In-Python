# There are following types of inheritance in oop:-

#1. Single Inheritance

class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")


# 2. Multiple Inheritance - one child class inherits from many parent classes.

class Father:
    def skills(self):
        print("Gardening")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    pass


# 3. Multilevel Inheritance

class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Puppy(Dog):
    def weep(self):
        print("Weeping")

# 4. Hierarchical Inheritance - All childs inherit from one parent
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Cat(Animal):
    def meow(self):
        print("Meowing")

# 5. Hybrid Inheritance (combination of two or more types)
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Pet:
    def play(self):
        print("Playing")

class Puppy(Dog, Pet):  # multilevel + multiple
    pass