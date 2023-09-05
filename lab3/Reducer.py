#!/usr/bin/env python2

import sys

current_country = None
min_rate = float('inf')
max_rate = float('-inf')

for line in sys.stdin:
    country, exchange_rate = line.strip().split('\t')
    exchange_rate = float(exchange_rate)

    # Check if the country has changed (next country encountered)
    if current_country and current_country != country:
        print(f"{current_country}\t{min_rate}\t{max_rate}")
        min_rate = float('inf')
        max_rate = float('-inf')

    current_country = country
    min_rate = min(min_rate, exchange_rate)
    max_rate = max(max_rate, exchange_rate)

# Don't forget to print the last country's result
if current_country:
    print(f"{current_country}\t{min_rate}\t{max_rate}")
