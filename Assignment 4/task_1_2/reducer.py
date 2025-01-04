#!/usr/bin/env python
import sys
from collections import defaultdict

word_count = defaultdict(int)

for line in sys.stdin:
    try:
        word, count = line.strip().split('\t', 1)
        count = int(count)
        word_count[word] += count
    except ValueError as e:
        sys.stderr.write(f"Error parsing line: {line} - {str(e)}\n")

for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:100]:
    print(f"{word}\t{count}")