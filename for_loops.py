#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

first_letter = 'p'
for fruit in fruits:
    if fruit.startswith(first_letter):
        print(fruit)
        break
else:
    print("NOT FOUND")
