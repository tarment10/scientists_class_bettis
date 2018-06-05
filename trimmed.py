#!/usr/bin/env python

def trimmed(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            line = line.rstrip('\n\r')
            yield line  # <1>

t = trimmed('DATA/mary.txt')
for line in t:  # <2>
    print(line)

