#!/usr/bin/env python

d1 = dict()  # empty dict
d2 = {'PIT': "Pittsburgh", 'ATL': 'Atlanta'}
d3 = {}

print(d2, '\n')
print(d2.keys())
print(d2.values())

for abbr, airport in d2.items():
    print(abbr, airport)
print()

for abbr, airport in sorted(d2.items()):
    print(abbr, airport)

x = list(d2.keys())
print(x)

ds = [1, 2, 3]

t1 = (i * 5 for i in ds)
t2 = (i + 2 for i in t1)
t3 = (i ** 2 for i in t2)

print(t3)

for i in t3:
    print(i)


for abbr, airport in sorted(d2.items()):
    print(abbr, airport)


d2['MIA'] = "Miami"
print(d2)
d2['MIA'] = "Miami, Florida"
print(d2)


del d2['PIT']

print(d2)

print(d2['ATL'])


print(d2.get('RDU'))

print(d2.get('RDU', 'NOT FOUND'))

x = None

print(x)
print(type(None))
print(bool(None))

print(d2.setdefault('RDU', 'Raleigh-Durham'))

print(d2)

