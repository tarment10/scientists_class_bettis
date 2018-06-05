#!/usr/bin/env python

p1 = 'Bob', 'Smith', 42
p2 = 'Liz', 'Collins', 38, 'CEO'
p3 = 'Joey', 'Vernecke', 11

print(p1[0], p2[0], p3[0], '\n')
people = [p1, p2, p3]

for p in people:
    print(p[0])
print()

first_name, last_name, age, *other = p1
print(first_name, last_name, '\n')

for _, last_name, age, *_ in people:
    print(last_name, age)
print()


values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z, '\n')

x, *y, z = values
print(x, y, z, '\n')

*x, y, z = values
print(x, y, z, '\n')





