#!/usr/bin/env python3

def is_ip_valid(ip_string):
    parts = ip_string.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
    return True

def is_port_valid(port_number):
    try:
        port = int(port_number)
        if 1 <= port <= 65535:
            return True
        else:
            return False
    except ValueError:
        return False

if __name__ == "__main__":
    test_ips = ["192.168.8.1", "192.80.9.0", "100.100"]
    test_port = ["800", 100, 200]

print("--- SOC IP VALIDATOR ---")
for ip in test_ips:
    result = is_ip_valid(ip)
    print(f"Testing IP {ip} : {result}")
print()
print("--- SOC PORT VALIDATOR ---")
for port in test_port:
    result = is_port_valid(port)
    print(f"Testing Ports {port} : {result}")
