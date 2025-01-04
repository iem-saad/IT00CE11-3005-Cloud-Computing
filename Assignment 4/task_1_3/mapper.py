#!/usr/bin/env python
import sys
from collections import defaultdict

# Dictionary to store local word length counts
local_word_count = defaultdict(int)

# Input comes from standard input (stdin)
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Split the line into words
    words = line.split()
    # Count words of length 3 and 5
    for word in words:
        word_length = len(word)
        if word_length == 3 or word_length == 5:
            local_word_count[word_length] += 1

# Output the local aggregated counts for lengths 3 and 5
for length, count in local_word_count.items():
    print(f"{length}\t{count}")