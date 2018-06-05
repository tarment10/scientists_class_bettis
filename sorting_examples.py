#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE" ]

f1 = sorted(fruits)
print(f1, '\n')

x = 'Wombat'
print(str.lower(x))
print(x.lower())
print()

f2 = sorted(fruits, key=str.lower)
print(f2, '\n')

f3 = sorted(fruits, key=len)
print(f3, '\n')

def len_and_name(f):
    return len(f), f.lower()

f4 = sorted(fruits, key=len_and_name)
print(f4, '\n')

f5 = sorted(fruits, key=lambda f: (len(f), f.lower()))
print(f5, '\n')


f6 = sorted(fruits, key=lambda f: list(reversed(f.lower())))
print(f6, '\n')

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

for first_name, last_name, brand in sorted(people, key=lambda e: (e[1], e[0])):
    print(first_name, last_name)
print()


