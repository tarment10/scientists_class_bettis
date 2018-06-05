#!/usr/bin/env python

x = 10

y = x or 50

print(y)

x = 0
y = x or 50

print(y)

#  A and B    A if A is False else B
#  A or  B    A if A is True  else B
