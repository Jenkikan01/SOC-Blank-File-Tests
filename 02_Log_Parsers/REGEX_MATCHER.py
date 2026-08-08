#!/usr/bin/env python3

import re

def log_line_parser(log_line):

    ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', log_line)

    timestamps = re.findall(r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}', log_line)

    alerts = re.findall(r'(?:WARNING|ERROR)\s+(\w+)', log_line)

    return {'ips':ips, 'timestamps':timestamps, 'alerts':alerts,}

test = [
"2024-01-15 09:12:33 Firewall BLOCK from 192.168.1.50 to 203.0.113.10",
"2024-01-15 09:15:01 Server WARNING timeout on port 443 from 10.0.0.5",
"2024-01-15 09:18:47 Application ERROR connection_refused on 172.16.5"
]

for i, lines in enumerate(test, start=1):
    results = log_line_parser(lines)
    print(f"Line {i}: {results}")
