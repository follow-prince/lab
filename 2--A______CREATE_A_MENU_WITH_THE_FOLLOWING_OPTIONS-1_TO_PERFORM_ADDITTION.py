def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y 

def display_menu():
    print("Welcome to the calculator!")
    print("Please choose an option:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

display_menu()

while True:
    choice = input("Enter your choice: ")

    if choice == '1':
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = add(num1, num2)
        print("The result is:", result)

    elif choice == '2':
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = subtract(num1, num2)
        print("The result is:", result)

    elif choice == '3':
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = multiply(num1, num2)
        print("The result is:", result)

    elif choice == '4':
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = divide(num1, num2)
        print("The result is:", result)

    elif choice == "5":
        break

    else:
        print("Invalid choice. Please choose (1/2/3/4/5).")

print("Thank you for using the calculator!")
