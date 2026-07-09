#                    Encapsulation

# Encapsulation helps to hide the internal implemetation details of a class by showing only necessary funcationalities.

# so making attributes  private / protected andaccessing them via getter/ setters is encapsulation

# NO encapsulation we can modify any data we want
class BadAccount:
    def __init__(self,balance):
        self.balance=balance

    
a1=BadAccount(0)
a1.balance=-1
print(a1.balance)

class GoodAccount:
    def __init__(self):
        self._balance=0.0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self,amount):
        if amount<=0:
            raise ValueError('Deposit Amount must be positive')
        self._balance+=amount

    def withdraw(self,amount):
        if amount<=0:
            raise ValueError ("With drawn amount must be positive")
        if amount>=self._balance:
            raise ValueError ("Insufficient Funds")
        self._balance-=amount

a2=GoodAccount()
print(a2.balance)
a2.deposit(200)
print(a2.balance)
a2.withdraw(100)
print(a2.balance)