#!/usr/bin/env python

mary_in = open('mary.txt')
mary_in.close()


with open('mary.txt') as mary_in:
    print(mary_in)
    print(mary_in.closed)

print("AFTER:")
print(mary_in)
print(mary_in.closed)

print('-' * 60)

with open('mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)

print('-' * 60)
with open('mary.txt') as mary_in:
    contents = mary_in.read()
print(contents)

print('-' * 60)
with open('mary.txt') as mary_in:
    all_lines = mary_in.readlines()
print(all_lines)

