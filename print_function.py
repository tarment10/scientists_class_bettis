#!/usr/bin/env python

x = 'kiwi'
y = 123.4
z = ['a', 'b', 'c']

print(x, y, z)
print("next line...")

#   str()   repr()
#  HUMAN    CODE

print(str(x), repr(x))

print(x)
print(y)
print(z)

print(x, end=" ")
print(y, end="")
print(z)

print(x, y, z, sep="/")

e = 'elk'
b = 'bear'
m = 'moose'

print(e, b, m)
print(e, b, m, sep=',')
print(e, b, m, sep=' <==> ')

