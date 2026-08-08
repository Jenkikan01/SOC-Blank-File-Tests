#!/usr/bin/env python3

print("=== SOC IP Menu Editor ===")

ip_addresses = ["192.168.8.1", "192.168.1.1", "192.167.0.3", "193.164.3.4", "192.164.66.9"]

while True:

    print("""--- IP Menu ---
1. Show all listed IPs
2. Add IP to the list
3. Remove IP from the list
4. Save the list to a file
5. Exit the program\n""" )

    choice = input("Select choices from 1 - 5: ")
    if choice == "1":
        for i, ip in enumerate(ip_addresses, start=1):
            print(f"{i}. {ip}")
        print(f"Total IP addresses is {len(ip_addresses)}\n")
    elif choice == "2":
        try:
            ip_add = int(input("Enter number of IP that you wanna add: "))
            for i in range(ip_add):
                ip_address = input(f"Enter IP Address #{i+1}: ")
                ip_addresses.append(ip_address)
                print("IP Address was added to the list!\n")
        except ValueError:
            print("Error Invalid Input please try again!")
    elif choice == "3":
        remove_ip = input("Enter IP Address you wanna remove from the list: ")
        if remove_ip in ip_addresses:
            ip_addresses.remove(remove_ip)
            print("IP Address was removed from the list!\n")
        else:
            print("IP address entered isnt on the list.")
    elif choice == "4":
        savefile = input("Enter the name of the file: ")
        with open(savefile, "w") as file:
            for i, ips in enumerate(ip_addresses, start=1):
                file.write(f"{i}: {ips} \n")
        print(f"IP list was saved to {savefile}!\n")
    elif choice == "5":
        print("Thank you for using the program!\nStay Vigilant!\nClosing the program...\nProgram closed\n.")
        break
    else:
        print("Entry invalid. Try again.")
