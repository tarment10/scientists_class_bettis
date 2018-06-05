#!/usr/bin/env python

class MyString(str):
    def startswith(self, *args):
        return 42


s = MyString()

print(s.startswith('x'))


