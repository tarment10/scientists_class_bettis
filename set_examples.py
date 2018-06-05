#!/usr/bin/env python

colors1 = ['red', 'pink', 'orange', 'purple', 'green']
colors2 = ['pink', 'purple', 'blue', 'black']

c1 = set(colors1)
c2 = set(colors2)
c2.add('brown')
c2.add('chartreuse')
c2.add('chartreuse')
c2.add('chartreuse')
c2.add('chartreuse')
c2.add('chartreuse')
c2.add('chartreuse')
c2.add('chartreuse')
c2.add('chartreuse')
c2.add('chartreuse')
c2.add('chartreuse')
c2.add('chartreuse')

print("both:", c1 & c2)
print("all:", c1 | c2)
print("either:", c1 ^ c2)
print("just c1:", c1 - c2)
print("just c2:", c2 - c1)

food = ['spam', 'spam', 'spam', 'spam',
        'egg', 'spam']

u = set(food)
print(u)


for color in c1:
    print(color)

fs = frozenset([1,2,3,4])

print(fs)
print(2 in fs)
print(22 in fs)

ls = { 5, 9, -3, 4}
print(ls)
ls.add(15)
print(ls)

s = set()
# s.add([1,2,3])
# print(s)

s.add(frozenset([1,2,3]))
s.add(frozenset([4,6,8]))

print(s)
