#!/usr/bin/env python

from datetime import date, timedelta, datetime

import time

today = date.today()
james_bd = date(2014, 8, 1)

delta = today - james_bd
print(delta, type(delta))


years, days = divmod(delta.days, 365.25)

print(f"James is {years} years and {days} days old")

add = timedelta(180)

print(today + add)

print(add.days)
print(add.seconds)
print(add.microseconds)

print(datetime.now())
print(datetime.now() + timedelta(0, 3900))

print(time.time())

print("Starting...", flush=True, end='')
time.sleep(2.6)
print("done!")
