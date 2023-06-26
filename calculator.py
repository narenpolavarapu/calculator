import time

def sum(num1, num2):
    return num1 + num2

def difference(num1, num2):
    return num1 - num2

def product(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num2 == 0:
        return "Error: Division by zero!"
    return num1 / num2


while True:
    print("Select an operation to perform:")
    print("1. Adding")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Calculator program exited.")
        print("-------------------")
        break

    if choice == '1':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        a = sum(num1, num2)
        print("Addition:", a)
        print("-------------------")
        time.sleep(1)
    elif choice == '2':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        a = difference(num1, num2)
        print("Subtraction:", a)
        print("-------------------")
        time.sleep(1)
    elif choice == '3':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        a = product(num1, num2)
        print("Multiplication:", a)
        print("-------------------")
        time.sleep(1)
    elif choice == '4':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        a = division(num1, num2)
        print("Division:", a)
        print("-------------------")
        time.sleep(1)
    else:
        print("input is out of range! try 1-5")
        print("-------------------")
        time.sleep(1)
