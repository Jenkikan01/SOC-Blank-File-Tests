#!/usr/bin/env python3

import os
import sys

log_dir = 'test_logs'

if not os.path.exists(log_dir):
    print("Directory not found!")
    sys.exit(1)

files = os.listdir(log_dir)
print("All files:", files)

print("Log files found:")
for filename in files:
    if filename.endswith('.log'):
        full_path = os.path.join(log_dir, filename)
        size = os.path.getsize(full_path)
        print(f"  {filename} - {size} bytes")

print("All .txt files (recursive):")
for root, dirs, filenames in os.walk(log_dir):
    for filename in filenames:
        if filename.endswith('.txt'):
            print(" ", os.path.join(root, filename))


target = os.path.join(log_dir, 'server.log')
if os.path.exists(target):
    print("server,log exists and can be opened")
    with open(target) as f:
        print("First line:", f.reaadline().strip())





