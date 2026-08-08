#!/usr/bin/env python3

print("=== SOC Report Writer ===")

report_title = input("Enter report title: ")
analyst_name = input("Enter analyst name: ")
date = input("Enter date of report: ")
findings = []

for i in range(1, 4):
    finding = input(f"Enter finding #{i}: " )
    findings.append(finding)
    print("Finding was added to the list!\n")
print(f"Saving list to {report_title}...")

with open(report_title, "w") as report:
    report.write("\n" + "=" * 40 + "\n")
    report.write(f"Report Title: {report_title}\n")
    report.write("=" * 40 + "\n")
    report.write(f"\n\nAnalyst: {analyst_name}\n")
    report.write(f"Date of the report: {date}\n")
    report.write("=" * 40 + "\n")
    report.write("FINDINGS:\n")
    for i, lines in enumerate(findings, start=1):
        report.write(f"{i}. {lines}\n")
    report.write("Report ends here.\n")
    report.write("=" * 40 + "\n")

with open(report_title, "r") as file:
    print(f"--- Displaying Report ---\n{file.read()}")
