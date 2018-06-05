#!/usr/bin/env python
import sys

from nnl.bettis.misc import bettislib as bl

bl.spam()
bl.ham()

for path in sys.path:
    print(path)
