#!/usr/bin/env python3

from ipaddress import ip_address

with open('web_access.log', 'r') as file:
    ip_counts = {}
    status_counts = {}
    for line in file:
        part = line.split()
        if len(part) < 2:      # skip blank/malformed lines
            continue
        ip = part[0]
        status = part[1]
        ip_counts[ip] = ip_counts.get(ip, 0) + 1
        status_counts[status] = status_counts.get(status, 0) + 1

print('=== IP COUNTS ===')
for ip, count in sorted(ip_counts.items(), key=lambda x: ip_address(x[0])):
    print(f"{ip}. {count}")

print('=== STATUS CODE COUNTS ===')
for status, count in sorted(status_counts.items(), key=lambda x: int(x[0])):
    print(f"{status}. {count}")

print('=== TOP 5 IPs BY FREQUENCY ===')
for ip, count in sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"{ip}. {count}")
