#!/usr/bin/env python
# (c) 2017 John Strickler
#
import h5py
import numpy as np

H5_FILE = '../DATA/h5/hdf5_test.h5'

a = np.array(
[[70, 31, 21, 76, 19, 5, 54, 66],
 [23, 29, 71, 12, 27, 74, 65, 73],
 [11, 84, 7, 10, 31, 50, 11, 98],
 [25, 13, 43, 1, 31, 52, 41, 90],
 [75, 37, 11, 62, 35, 76, 38, 4]]
)


with h5py.File(H5_FILE) as hfile:
    ds1 = hfile.create_dataset('/Animals/wombat', (15, 2))
    ds2 = hfile.create_dataset(
        '/Animals/bushbaby', (40, 3), dtype='i8'
    )
    ds3 = hfile.create_dataset(
        'init', data=a
    )

