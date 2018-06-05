#!/usr/bin/env python

x = 45

if x > 50:
    print("whale")
    print("wolverine")
elif x > 40:
    print("erne")
    print("porcupine")
    if x > 42:
        print("spam")
else:
    print("button")
    print("gewgaw")

# FALSE VALUES:
#  False  None   0.0  0
#  ""  [] {} set() ()

def spam(x=None):
    if x is None:
        x = []
    x.append(5)
    print(x)

spam()
spam()
spam()
print()

def ham(x=[]):
    x.append(5)
    print(x)

ham()
ham()
ham()

#  == !=  >  <  >= <=

#  and or not

#  if x:
#     ....





