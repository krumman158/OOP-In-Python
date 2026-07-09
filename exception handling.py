#                                      Custom Exception Classes

# Custom exceptions = user-defined exception classes (inheriting from Exception) for specific error handling.

class InsufficientBalanceError(Exception):
    def __init__(self, message="Balance is too low"):
        self.message = message
        super().__init__(self.message)

class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Not enough funds!")
        self.balance -= amount

acc = Account(100)
try:
    acc.withdraw(200)
except InsufficientBalanceError as e:
    print(e)  # Not enough funds!