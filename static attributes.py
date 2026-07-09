#                                        Static Attributes

# We know that each instance(object) of a class can have unique attrubutes but we can some static attributes among all objects.

# Static attributes belong to a class not to a specific instance of that class.

# Static attributes have only one copy in memory regardless of num of insatnces.

# Can be accessed by class itself and objects.

class User:
    user_count=0

    def __init__(self,name,email):
        self.name=name
        self.email=email
        User.user_count+=1

    def display(self):
        print(f"User name: {self.name}Email: {self.email}")

u1=User('Rumman','rum@gmail.com')
u2=User('Abdullah','abd@gmail,com')

print(User.user_count)
print(u1.user_count) # can also be accessed by objects as it is a shared attribute
print(u2.user_count)