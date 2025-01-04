#!/usr/bin/env python
import sys
from collections import defaultdict

# Dictionary to store total counts
total_counts = defaultdict(int)

for line in sys.stdin:
    try:
        key, value = line.strip().split('\t')
        total_counts[key] += int(value)
    except ValueError as e:
        sys.stderr.write(f"Error parsing line: {line} - {str(e)}\n")

# Get the total number of requests and bytes transferred
total_requests = total_counts.get("total_requests", 0)
total_bytes = total_counts.get("total_bytes", 0)

# Calculate costs based on the total requests and total bytes
cost_requests = total_requests * 0.001
total_gbs = total_bytes / (1024 ** 3) 
cost_data = total_gbs * 0.08


print(f"Total Requests: {total_requests}")
print(f"Total Bytes Transferred: {total_bytes} bytes")
print(f"Total Transfer in terms of GB: {total_gbs:.4f} GB")
print(f"Total Cost for Requests: {cost_requests:.4f} EUR")
print(f"Total Cost for Data Transferred: {cost_data:.4f} EUR")
print(f"Total CDN cost: {cost_requests + cost_data:.4f} EUR")