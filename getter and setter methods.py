# To modify protected/private attributes we must use getters and setters methods. Protected attributes can be accessed outside the class but as a python developer we must respect the convention. 

# Getter and setter also provides us a single point where we want to modify/access our data and to implemet all logic.

# we use private and protected beacuse to protect the access of sensitive data. Via getter methods we can have details when this sensitive data was accessed and by whom. Can also save this to a log file. We can define who can access this sensitive data.

# Via setter methods we can define logic that sensitive data was set to correct format.

from datetime import datetime
class User:
    def __init__(self,name,email,password):
        self.name=name
        self._email=email
        self.__password=password

    def get_email(self):
        print(f'Email was accessed at {datetime.now()}')
        return self._email
    
    def set_email(self,new_email):
        if "@" in new_email:
            self._email=new_email
            print("Email Updated")
        else:
            print("Invalid email address. Email not Updated")
    
u1=User('Danny','dan@gmail.com','111-22')

print(u1.get_email())
u1.set_email("111")
u1.set_email('dan@outlook.com')
print(u1.get_email())

# The getter and setter implemented in this code is java/c style python has a easy way of doing so. Which is in decorators.py