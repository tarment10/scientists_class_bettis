#!/usr/bin/env python

i1 = 100
i2 = 0x100
i3 = 0b100
i4 = 0o100

print(i1, i2, i3, i4)

f1 = 123.456
f2 = 123.
f3 = .456
f4 = 1.234e55

#  int() float()
#  bool()  str() repr()

x = 123.456
y = "358"
print(int(x), int(y))

z = "DeadBeef"

print(int(z, 16))
print(int(z, 23))

#  + - * /  ** // %

print(25/3)
print(25//3)

print(2 ** 5, 5 ** 2)
