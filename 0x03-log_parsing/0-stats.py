#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''

import sys
import signal

# Define status codes
status_codes = {200, 301, 400, 401, 403, 404, 405, 500}

# Initialize metrics
total_file_size = 0
status_code_count = {code: 0 for code in status_codes}

def print_statistics():
    print(f"Total file size: File size: {total_file_size}")
    for code in sorted(status_codes):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")

def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        parts = line.strip().split()
        if len(parts) == 7 and parts[5].isdigit():
            ip_address, date, _, status_code, file_size = parts[0], parts[3][1:], parts[5], int(parts[6])
            if int(status_code) in status_codes:
                total_file_size += file_size
                status_code_count[int(status_code)] += 1

        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    signal_handler(signal.SIGINT, None)

