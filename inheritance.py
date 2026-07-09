#                     Inheritance

# It is relationship between classes and their sub classes

class Vehicle:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def start(self):
        print("Vehicle strated")

    def stop(self):
        print("Vehicle stopped")

class Car(Vehicle):
        def __init__(self, brand, model, year,doors,engine):
             # super is used to inherit parent's attributes
             super().__init__(brand, model, year)
             self.doors=doors
             self.engine=engine

class Bike(Vehicle):
     def __init__(self, brand, model, year,engine):
          super().__init__(brand, model, year)
          self.engine=engine

car=Car('Ford','Focus',2026,4,'1300cc')
bike=Bike('Honda','CG-125',2026,'125cC')

car.start()
bike.start()