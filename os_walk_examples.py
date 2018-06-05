#!/usr/bin/env python

#!/usr/bin/env python

import os

TARGET = '.'

for dir_name, sub_dirs, files in os.walk(TARGET, topdown=True):
    print(dir_name)
    if dir_name.count('/') > 0:  # like depth option to find
        sub_dirs.clear()
    for file_name in files:
        if file_name.endswith('.py'):
            file_path = os.path.join(dir_name, file_name)
            file_size = os.path.getsize(file_path)
            print('{:8d} {}'.format(file_size, file_name))
