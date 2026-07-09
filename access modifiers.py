# Access Modifiers:
# There are mainly three types of access modifiers i:e public, protected and private. Public data can be accessd anywhere in the code. Private/Protected data should only be accessed within a class.
# email -> public _email -> protected and __email -> private (name-mangled variables)

class User:
    def __init__(self,username,email,password):
        self.username=username
        self._email=email
        self.__password=password

    def clean_email(self):
        return self._email.lower().strip()
    def return_password(self):
        return self.__password

u1=User('Danny',' Dan@gmail.com','123')
print(u1._email) # we can access protected attributes outside class in python but you must not do that. 

print(u1.clean_email())

print(u1.return_password())
print(u1.__password) # throws error. Private attributes can not be accessed outside the class