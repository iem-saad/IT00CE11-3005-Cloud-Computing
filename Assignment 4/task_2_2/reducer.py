#!/usr/bin/env python
import sys
from collections import defaultdict

domain_count = defaultdict(int)

for line in sys.stdin:
    try:
        domain, count = line.strip().split('\t')
        domain_count[domain] += int(count)
    except ValueError as e:
        sys.stderr.write(f"Error parsing line: {line} - {str(e)}\n")

# Sort the domains by count and get the top 5
top_domains = sorted(domain_count.items(), key=lambda x: x[1], reverse=True)[:5]

print("\nTop 5 Domain Names:")
for domain, count in top_domains:
    print(f"{domain}: {count}")