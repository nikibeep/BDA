#!/usr/bin/env python3

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file=sys.stdin):
    for line in file:
        yield line.strip().split('\t', 1)

def main():
    data = read_mapper_output()
    for current_item, item_count in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for _, count in item_count)
            print(f"{current_item}\t{total_count}")
        except ValueError:
            pass

if __name__ == "__main__":
    main()
