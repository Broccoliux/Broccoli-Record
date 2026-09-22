'''Calling functions
To use a function, call it by name with parentheses:
'''

def say_goodbye():
    print("Goodbye!")
    print("See you later!")

# Call it multiple times
say_goodbye()
say_goodbye()
say_goodbye()



''''Functions with logic
Functions can contain any Python code:
'''

def check_weather():
    temperature = 25
    if temperature > 30:
        print("It's hot!")
    else:
        print("Nice weather!")

# Use the function
check_weather()


'''Local variables
Variables created inside a function only exist within that function:
'''

def calculate_price():
    price = 199999
    tax = price * 0.07
    total = price + tax
    print("total price:", total)

calculate_price()

# ------------------ #
name = input("What is your name? ")
def greet_alice():
    print("Hello, Alice!")

def greet(name):
    print(f"Hello, {name}!")

greet(name)  # Call the function with the user's input


'''Modifying global variables
To change a global variable inside a function, use the global keyword:
'''

counter = 0  # Global variable

def increment():
    global counter  # Declare we want to modify the global variable
    counter += 1

increment()

print(counter)  # 3



# Bad - using global variable
total = 0

def add_to_total(amount):
    global total
    total += amount

# Good - using parameters and return
def add_amounts(current_total, amount):
    return current_total + amount

total = 0
total = add_amounts(total, 10)
total = add_amounts(total, 20)
print(total)  # 30


'''Multiple parameters
Functions can have multiple parameters:
'''

def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")

calculate_total(100, 0.08, 10)



def calculate_total(price, discount):
  tax_rate = 0.8

  tax = price * tax_rate
  final_price = price + tax - discount

  print(f"Total: ${final_price}")
calculate_total(price=100, discount=10)

'''Keyword arguments
Call functions using parameter names for clarity:
'''

def create_profile(name, age, city):
    print(f"{name}, {age}, from {city}")

# Positional arguments (order matters)
create_profile("Alice", 25, "NYC")

# Keyword arguments (order doesn't matter)
create_profile(city="NYC", age=25, name="Alice")
create_profile(name="Bob", city="LA", age=30)
