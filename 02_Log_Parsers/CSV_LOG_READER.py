#!/usr/bin/env python3

import csv

while True:
    request = input("Enter file name: \n>")
    try:
        with open(request, 'r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)
            print(f"HEADER: {header}")
            print("---")
            for i, row in enumerate(reader, start=1):
                print(f"ROW {i}: {row}")
            break
    except FileNotFoundError:
        print(f"File not found please try again!")

# use the following block of code to create a .csv file:
#    timestamp,source_ip,destination_ip,port,status
#    2024-01-15 08:23:14,192.168.1.105,203.0.113.45,80,ALLOW
#    2024-01-15 08:24:02,10.0.0.15,198.51.100.22,443,BLOCK
#    2024-01-15 08:25:33,192.168.1.110,203.0.113.45,22,ALLOW
#    2024-01-15 08:26:11,172.16.0.5,198.51.100.88,53,ALLOW
