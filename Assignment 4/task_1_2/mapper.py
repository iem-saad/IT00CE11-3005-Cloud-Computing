#!/usr/bin/env python
import sys
from collections import defaultdict

local_word_count = defaultdict(int)

for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Split the line into words
    words = line.split()
    # Increment local count for each word (the combiner)
    for word in words:
        local_word_count[word] += 1

# Output the local aggregated counts
for word, count in local_word_count.items():
    print(f"{word}\t{count}")