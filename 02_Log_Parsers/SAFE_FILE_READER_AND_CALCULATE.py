#!/usr/bin/env python3

print("=== Safe Division ===")

try:
    dividend = float(input("Enter Dividend: "))
    divisor = float(input("Enter Divisor: "))
    print(f"Result: {dividend} / {divisor} = {dividend/divisor:.2f}\n")
except ValueError:
    print("Error: Enter valid numbers only.\n")
except ZeroDivisionError:
    print("Error: Cannot be divided by zero. Try again.\n")


print("===Safe File Read===")

try:
    request = input("Enter file name (Try 'soc_logs.txt'): ")
    with open(request, "r") as file:
        sentence = file.readlines()
        for i, lines in enumerate(sentence, start=1):
            clean_lines = lines.strip()
            print(f"{i}. {clean_lines}")
    print()
except FileNotFoundError:
    print("Error: File not found.\n")

except PermissionError:
    print("Error: Permission Denied for this file.\n")

print("===Safe read with calculate===")

try:
    request = input("Enter filename you wish to open with a number: ")
    divisor = float(input("Enter here the number: "))
    with open(request, "r") as file:
        lines = file.read()
        print(f"""Total lines: {len(lines)}
Calculation = {len(lines)} / {divisor} = {len(lines)/divisor:.2f})
Program Complete No Crashes!""")

except ZeroDivisionError:
    print("Error: Cannot be divided by zero.")
except ValueError:
    print("Error: Invalid value entered.")
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"Unexpected Error as {e}")
