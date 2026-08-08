#!/usr/bin/env python3

ip_data = {}

with open('network_logs.txt', 'r') as file:
    for line in file:
        part = line.split()
        timestamp = ' '.join(part[0:2])
        ip = part[2]
        port = part[3]
        status = part[4]

        if ip not in ip_data:
            ip_data[ip] = {
                'count': 0,
                'first_seen': timestamp,
                'last_seen': timestamp,
                'ports': [],
                'statuses': []
            }

        ip_data[ip]['count'] += 1
        ip_data[ip]['last_seen'] = timestamp
        ip_data[ip]['ports'].append(int(port))
        ip_data[ip]['statuses'].append(status)

for ip, data in ip_data.items():
    print("---")
    print(f"IP: {ip}")
    print(f"Counts: {data['count']}")
    print(f"First Seen: {data['first_seen']}")
    print(f"Last Seen: {data['last_seen']}")
    print(f"Ports: {data['ports']}")
    print(f"Status: {data['statuses']}")
    print("---")
