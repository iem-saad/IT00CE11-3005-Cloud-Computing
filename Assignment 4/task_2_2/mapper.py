#!/usr/bin/env python
import sys
import re

# Input comes from standard input (stdin)
for line in sys.stdin:
    line = line.strip()
    
    # Regular expression to match the log entry format
    match = re.match(r'(\S+) - - \[(.*?)\] "(.*?)" (\d+) (\d+|-)', line)
    
    if match:
        client_name = match.group(1)

        # Check if the client name is an IP address or a domain name
        if re.match(r'^\d+\.\d+\.\d+\.\d+$', client_name):
            continue  # Skip if it's an IP address

        # Split the client name by '.' to get domain parts
        parts = client_name.split('.')
        
        # Ensure there are at least two parts to form a domain
        if len(parts) >= 2:
            # Join the last two parts for the domain name
            domain = '.'.join(parts[-2:])  # This will handle multiple segments correctly
            # Emit the domain with a count of 1
            print(f"{domain}\t1")