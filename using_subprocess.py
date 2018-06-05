#!/usr/bin/env python
from glob import glob
import shlex
from subprocess import run, CalledProcessError, PIPE, check_call, check_output

try:
    proc = run(["netstat", "-an"], stdout=PIPE, stderr=PIPE)
except CalledProcessError as err:
    print(err, err.returncode)

print(proc.stdout.decode())
print(proc.returncode)
print(proc.args)

files = glob('DATA/*.txt')
print(files)

cmd = """foo 'big hen', 'red balloon' 1 2 3"""
print(shlex.split(cmd))
