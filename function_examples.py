#!/usr/bin/env python

def get_message():
    return "Hello, world"

def show_message():
    m = get_message()
    print(m)

show_message()

def shout_message(message):
    print(message.upper())
    # if isinstance(message, str):
    #     print(message.upper())
    # else:
    #     raise TypeError("message must be a string")


msg = get_message()
shout_message(msg)


def greet_people(greeting, *people, shout=False):
    if shout:
        greeting = greeting.upper()
    for person in people:
        print(greeting, person)
print()

greet_people("Hi", "Mom")
print()

greet_people("Hello", "Mom", "Dad", shout=False)
print()

greet_people("What's up", "Mom", "Dad", "Dorothy", "Auntie Em", shout=True)
print()

greet_people("Hi There", shout=True)
print()

def config(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

config(filename="wombat.txt", user="cdundee")
print()

config()
print()


def doit(*, filename, username):
    print("filename:", filename)
    print("username:", username)


doit(username='Bob', filename='foo.txt')
doit(filename="bar.txt", username='Gandalf')

print()

def wacky(p1, p2, *p3, p4, p5, **p6):
    pass









