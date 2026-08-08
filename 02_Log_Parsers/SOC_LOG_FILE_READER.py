#!/usr/bin/env python3

print("=== SOC Log File Reader ===\n")
print()
print("--- Read file with .read()")
with open("soc_logs.txt", "r") as file:
    print(file.read())

print("--- Read file with .readlines()")
with open("soc_logs.txt", "r") as file:
    line = file.readlines()
    for i, lines in enumerate(line, start=1):
        clean_lines = lines.strip()
        print(f"{i}. {clean_lines}")
    print(f"\nTotal lines: {len(line)}")

