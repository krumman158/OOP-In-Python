# class like a blue print that define what kind of attributes, methods or behavior the object of this class will have
class Dog:
# __init__ runs only once when object of a class is created and initializes that object with class attributes and methods.
# So each object can have different methods and attributes.

# instance is object of class.

# `self` refers to the specific instance calling the method — lets it access/modify that instance's own attributes (like `name`, `breed`).
    def __init__(self,name,breed,owner):
        self.name=name
        self.breed=breed
        self.owner=owner

    def bark(self):
        print("WHOOF WHOOF")

class Owner:
    def __init__(self,name,contact_number):
        self.name=name
        self.contact_number=contact_number

# we can have a relationship between objects of different classes and can acces one oject in another object via its class name
owner1=Owner('Danny','888-999')    
dog1=Dog("Bruce","Scottish",owner1)
dog1.bark()
print(dog1.name)
print(dog1.breed)
print(dog1.owner.name,'\n')

owner2=Owner('Sally',111-222)
dog2=Dog("Henry","German",owner2)
dog2.bark()
print(dog2.name)
print(dog2.breed)
print(dog2.owner.name,'\n')