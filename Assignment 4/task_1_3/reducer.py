#!/usr/bin/env python
import sys
from collections import defaultdict

total_word_count = defaultdict(int)

for line in sys.stdin:
    try:
        length, count = line.strip().split('\t')
        total_word_count[int(length)] += int(count)
    except ValueError as e:
        sys.stderr.write(f"Error parsing line: {line} - {str(e)}\n")

# Output the total counts for words of length 3 and 5
for length, count in total_word_count.items():
    print(f"Words of length {length}: {count}")