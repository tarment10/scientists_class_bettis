#!/usr/bin/env python
# (c) 2017 John Strickler
#
import h5py
import numpy as np

H5_FILE = '../DATA/h5/hdf5_test.h5'

H5_DATASET = '/arrays/2D int8x9'

with h5py.File(H5_FILE) as hfile:

    dset = hfile[H5_DATASET]

    # for row in dset:
    #     print(row)

    for i, row in enumerate(dset):
        print("ROW {}: {}".format(i, row))
    print()

    print("type of dset:", type(dset))

    print("Row 0:")
    print(dset[0])
    print()


    print("Column 1:")
    print(dset[:,1])
    print()

    print("Rows 3 & 4, Columns 5 & 6")
    print(dset[3:5, 5:7])

    result = np.mean(dset[:3])
    print(result)

    dset[0,0] = 5

    for i in range(3, 7):
        dset[0,i] = 1000


