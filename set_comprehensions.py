#!/usr/bin/env python

items = ['Spam', 'spam', 'Spam','spam', 'Spam',
  'Eggs', 'eggs', 'Spam', 'SPAM', 'SPAM', 'EGGS',
         'swedish meatballs']

i1 = set(items)
print(i1, '\n')

i2 = {i.lower() for i in items if len(i) < 5}
print(i2, '\n')

dc1 = {i.lower(): len(i) for i in items}
print(dc1, '\n')
