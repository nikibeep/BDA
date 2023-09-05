#!/usr/bin/env python2

import sys

for line in sys.stdin:
    name, number = line.strip().split(' ')
    print('{}\t{}'.format(number, name))
