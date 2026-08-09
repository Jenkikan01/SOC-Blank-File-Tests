#!/usr/bin/env python3

connections = [
    "192.168.1.1:80",
    "10.0.0.1:443",
    "172.16.0.5:8080",
    "192.168.1.50:22",
    "8.8.8.8:53",
    "10.10.10.1:3389"
]

ips_only = [conn.split(':')[0] for conn in connections]

ports_only = [int(conn.split(':')[1]) for conn in connections]

high_ports = [conn for conn in connections if int(conn.split(':')[1]) > 1024]

ten_net = [conn for conn in connections if conn.startswith('10.')]

count_even = sum([1 for conn in connections if int(conn.split(':')[1]) % 2 == 0])

print(f"""
IPS: {ips_only}
PORTS: {ports_only}
HIGH PORTS (above 1024): {high_ports}
10.x.x.x ENTRIES: {ten_net}
EVEN PORTS: {count_even}
""")
