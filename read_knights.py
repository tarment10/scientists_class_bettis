#!/usr/bin/env python
from pprint import pprint

all_knights = []
with open('DATA/knights.txt') as knights_in:
    for line in knights_in:
        fields = line.rstrip().split(':')
        all_knights.append(fields)
        print(fields[0])

pprint(all_knights)
