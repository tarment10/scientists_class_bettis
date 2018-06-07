#!/usr/bin/env python

class Spam():
    def bark(self):
        print("Woof!")

class Ham(Spam):
    pass

print(Ham.mro())
h = Ham()
h.bark()

def doit(spam):
    # if type(spam) == Spam:
    if isinstance(spam, Spam):
        print("GOOD")
    else:
        print("BAD")

s = Spam()
doit(s)
doit(h)
