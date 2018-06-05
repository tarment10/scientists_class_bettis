#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

print(len(fruits))
print(fruits[0], fruits[3], fruits[len(fruits)-2])
print(fruits[3:7])
#  sequence[:stop]
#  sequence[start:]
#  sequence[start:stop]
#  sequence[start:stop:step]

print(fruits[4:])


nums = [800,80,1000,32,255,400,5,5000]

n = [float(i) for i in nums if i > 100 if i < 1000]
print(n)

e = []

e = list()

words = 'foo bar blah'.split()

e.append('wombat')
e.append('bushbaby')
e.append('coatimundi')

print(e)

e.insert(0, 'koala')
e.insert(-2, 'kookaburra')

print(e)
del e[3]
print(e)

e.remove('koala')
print(e)

x = e.pop(2)
print(x)
print(e)

more_creatures = ['giraffe', 'rhino', 'hippo']

e.extend(more_creatures)

print(e)
print()

for creature in e:
    print(creature, len(creature), creature.upper())



