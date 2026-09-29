class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print(self.__balance)

account = BankAccount(5000)

account.show_balance()


# @property

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

account = BankAccount(5000)

print(account.balance)


# setter

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount

account = BankAccount(5000)

print(account.balance)   # Read
account.balance = 10000  # Change
print(account.balance)



#  @classmethod

