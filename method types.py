# mehtods can also be public, protected and private just like the attributes

class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        if self._is_valid_amount(amount):
            self._balance+=amount
            self.__transaction("deposit",amount)
        else:
            print("Deposit amount must be positive")

     # protected amount
    def _is_valid_amount(self,amount):
        return amount>=0
    
    # private method
    def __transaction(self,transaction_type,amount):
        print(f"Logging  {transaction_type} of {amount}.New Balance is {self.balance}")

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0<= rate <=5
    

a1=BankAccount('Rumman',500)
