#!/usr/bin/env python2

import sys

current_number = None
name_list = []

for line in sys.stdin:
    number, name = line.strip().split('\t')
    
    if current_number == None:
        current_number = number
        
    if current_number != number:
        name_list.sort()
        for n in name_list:
            print('{}\t{}'.format(n, current_number))
        current_number = number
        name_list = []
    
    name_list.append(name)

# Don't forget to print the last batch of names for the last number
if current_number != None:
    name_list.sort()
    for n in name_list:
        print('{}\t{}'.format(n, current_number))
