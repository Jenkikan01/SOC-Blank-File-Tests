#!/usr/bin/env python3

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Zero Division")
        return None

def calculator():
    while True:
        print("""--- Choices ---\n
1.) Addition
2.) Subtract
3.) Multiply
4.) Division
5.) Close""")

        choice = input("Enter choice: ")

        if choice == "1":
            a = float(input("Enter number: "))
            b = float(input("Enter number: "))
            print(f"'Result: {add(a, b):.2f}'")
            print()

        elif choice == "2":
            a = float(input("Enter number: "))
            b = float(input("Enter number: "))
            print(f"'Result: {subtract(a, b):.2f}'")
            print()

        elif choice == "3":
            a = float(input("Enter number: "))
            b = float(input("Enter number: "))
            print(f"'Result: {multiply(a, b):.2f}'")

        elif choice == "4":
            a = float(input("Enter number: "))
            b = float(input("Enter number: "))
            result = divide(a, b)
            if result is not None:
                print(f"'Result: {divide(a, b):.2f}'")

        elif choice == "5":
            print("Program Exit...")
            break

if __name__ == "__main__":
    calculator()
