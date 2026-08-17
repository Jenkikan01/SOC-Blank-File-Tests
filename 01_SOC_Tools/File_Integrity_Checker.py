#!/usr/bin/env python3

import hashlib

def calculate_sha256(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, 'rb') as file:
        while chunk := file.read(4096):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def compare_files(file1, file2):
    hash1 = calculate_sha256(file1)
    hash2 = calculate_sha256(file2)
    if hash1 == hash2:
        print(f"MATCH: {file1} and {file2} are identical")
    else:
        print(f"MISMATCH: {file1} and {file2} are different!")

if __name__ == "__main__":
    compare_files('file_a.txt', 'file_b.txt')
    compare_files('file_a.txt', 'file_a.txt')
