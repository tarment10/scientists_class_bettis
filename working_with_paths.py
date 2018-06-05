#!/usr/bin/env python
import os
from datetime import datetime

FOLDER = 'DATA'
FILE_NAME = 'alice.txt'

file_path = os.path.join(FOLDER, FILE_NAME)

print("file path:", file_path)

print("dir name:", os.path.dirname(file_path))
print("base name:", os.path.basename(file_path))
print("abs path:", os.path.abspath(file_path))

print("file size", os.path.getsize(file_path))

raw_timestamp = os.path.getmtime(file_path)
print("raw timestamp:", raw_timestamp)
timestamp = datetime.fromtimestamp(raw_timestamp)
print("mod time:", timestamp)
print("mod time:", timestamp.strftime('%m/%d/%y'))

stat_info = os.stat(file_path)
print(stat_info)

if os.path.exists('DATA/mary.txt'):
    os.remove('DATA/mary.txt')

if not os.path.exists('wombat'):
    os.mkdir('wombat')

os.makedirs("foo/bar/blah", exist_ok=True)

print(os.access('DATA/alice.txt', os.R_OK | os.W_OK))


