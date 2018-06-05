#!/usr/bin/env python

i = 0
while i < 4:
    print(i)
    i += 1

while True:
    name = input("What is your name? (or q to quit) ")
    if name == 'q':
        break
    if name == '':
        continue
    print("Hi, {}".format(name))
