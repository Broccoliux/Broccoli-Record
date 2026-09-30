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

class Car:
    wheels = 4

    @classmethod
    def show_wheels(cls):
        print(cls.wheels)

Car.show_wheels()



class Car:
    wheels = 4

    def show_car(self):
        print("This is an object method")

    @classmethod
    def show_wheels(cls):
        print(cls.wheels)

    @staticmethod
    def add(a, b):
        return a + b

car = Car()
car.show_car()


# __str__

class Car:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"Car: {self.brand}"

car = Car("Toyota")

print(car)


# __len__

class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

team = Team(["Ali", "Ahmed", "Sara"])

print(len(team))


