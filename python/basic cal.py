num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print(num1 + num2)

elif choice == 2:
    print(num1 - num2)

elif choice == 3:
    print(num1 * num2)

elif choice == 4:
    print(num1 / num2)

else:
    print("Invalid choice")
