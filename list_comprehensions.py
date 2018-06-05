#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE" ]

f0 = []
for f in fruits:
    if f.lower().startswith('p'):
        f0.append(f.upper())
print(f0, '\n')

f1 = [f.upper() for f in fruits if f.lower().startswith('p')]
print(f1, '\n')

f2 = [f.upper() for f in fruits]
print(f2, '\n')

f3 = [f for f in fruits if f.lower().startswith('p')]
print(f3, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]

last_names = [p[1] for p in people]
print(last_names, '\n')

names = [f"{fname} {lname}" for fname, lname, _ in people]
print(names, '\n')

nums = [800,80,1000,32,255,400,5,5000]

n1 = [float(i) for i in nums if i > 200]
print(n1)
