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


# __eq__

class Car:
    def __init__(self, brand):
        self.brand = brand

    def __eq__(self, other):
        return self.brand == other.brand


car1 = Car("Toyota")
car2 = Car("Toyota")
car3 = Car("Honda")

print(car1 == car2)
print(car1 == car3)



# *args


def add(*args):
  return sum(args)

print(add(1, 2))
print(add(1,2,4,5))


# **kwargs

def show_info(**kwargs):
    print(kwargs)

show_info(name="Broccoli", age= 19, city="bahawalpur")


# Decorators @

def log_function(func):
    def wrapper():
        print("Function start")
        func()
        print("Function end")
    return wrapper


@log_function
def hello():
    print("Hello")


hello()


# Generators — yield

def numbers():
    yield 1
    yield 2
    yield 3

for number in numbers():
    print(number)




# try and except

try:
    print("Running")
except:
    print("Error")
finally:
    print("Finished")
