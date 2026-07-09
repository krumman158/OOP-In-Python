#                                            @property
# @property is a standard way of making getters in python.
# we can use @property when we want to all objects to access attribuye by its name and we don't have to define setter and getter methods i:e u1.get_email etc.

# It also helps us to change code in one place rather than changing the objects accessing attributes. we also dont have to put () for proptery functions.

# So u1.email looks we are directly accessing email attribute but bts we are accessing property. It also keeps the things simple than getters and setters.

# just implement setter and getter via attribute name and keep things simpler

class User:
    def __init__(self,name,email,password):
        self.name=name
        self._email=email
        self.__password=password

    @property
    def email(self):
        print("Email accessed")
        return self._email
    
    @email.setter
    def email(self,new_email):      
        if '@' in new_email:
            self._email=new_email

u1=User('Danny','dan@gmail.com','11-22')

print(u1.email)
u1.email='dan@outlook.com'
print(u1.email)