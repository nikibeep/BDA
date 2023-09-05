# Mapper.py



#!/usr/bin/env python2



import sys



for line in sys.stdin:

    # Remove leading and trailing whitespace and split the line into fields

    fields = line.strip().split(',')

    

    # Check if the line contains column names (header)

    if fields[0] == "Date":

        continue

    

    # Extract country and exchange rate from the CSV columns

    country = fields[1]

    exchange_rate = float(fields[2])

    

    # Emit the key-value pair (country, exchange_rate)

    print("{}\t{}".format(country, exchange_rate))



