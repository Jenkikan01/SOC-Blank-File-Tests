#!/usr/bin/env python3

print("=== SOC IP LIST PROCESSOR ===")
ip_addresses = ["192.168.8.1", "192.168.1.1", "192.168.9.1", "192.167.44.0", "192.178.0.1"]

print("Initial IP Addresses List:")
print(f"Total number of IP addresses:{len(ip_addresses)}.")
for i, ip in enumerate(ip_addresses):
    print(f"{i}. {ip}")
print()
request = int(input("Enter number of IP addresses you want to add: "))
print()

for i in range(request):
    new_ip = input(f"Enter new IP Address #{i+1}. ")
    ip_addresses.append(new_ip)
    print("New IP Address added!")
print()

print("New IP Addresses List:")
for i, ip in enumerate(ip_addresses):
    print(f"{i}. {ip}\n")
print()

print(f"""=== SUMMARY STATISTICS ===
Total Number of IP Addresses: {len(ip_addresses)}
First IP Address: {ip_addresses[0]}
Last IP Address: {ip_addresses[-1]}""")
