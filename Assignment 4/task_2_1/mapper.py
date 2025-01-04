#!/usr/bin/env python
import sys
import re

# Regular expression to match the log entry format
log_pattern = re.compile(r'(\S+) - - \[(.*?)\] "(.*?)" (\d+) (\d+)')

for line in sys.stdin:
    line = line.strip()
    
    # Count the request even if it doesn't match the exact format
    print(f"total_requests\t1")
    
    # Try to match the log entry format to extract bytes transferred
    match = log_pattern.match(line)
    
    if match:
        # Extract bytes transferred
        bytes_transferred = match.group(5)
        
        # Check if bytes_transferred is not '-', emit the byte count
        if bytes_transferred != '-':
            print(f"total_bytes\t{bytes_transferred}")
