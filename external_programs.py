#!/usr/bin/env python
import os

#  os.system("cmd ....")
#  obj = os.popen("cmd ....")

# os.system("netstat -an")
# print()

with os.popen("netstat -an") as netstat_in:
    for line in netstat_in:
        if 'ESTAB' in line:
            print(line, end='')

