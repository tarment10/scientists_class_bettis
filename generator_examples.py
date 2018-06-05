#!/usr/bin/env python

with open('DATA/mary.txt') as mary_in:
    for line in mary_in:
        print(repr(line))
print()

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE" ]

f1 = [f.lower() for f in fruits if f.lower().startswith('p')]
for fruit in f1:
    print(fruit)
print()

fg1 = (f.lower() for f in fruits if f.lower().startswith('p'))
for fruit in fg1:
    print(fruit)
print()


g1 = (f.lower() for f in fruits)
g2 = (f for f in g1 if f.lower().startswith('p'))

for fruit in g2:
    print(fruit)
print()
