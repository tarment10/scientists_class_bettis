#!/usr/bin/env python
# (c) 2017 John Strickler
#
import h5py
import numpy as np

H5_FILE = '../DATA/h5/hdf5_test.h5'

hfile = h5py.File(H5_FILE)

print('groups:')
for group in hfile:
    print(group)
print()

print('datasets in /arrays:')
for dataset in hfile['arrays']:
    print(dataset)

dset = hfile['/Animals/bushbaby']

x = np.array(dset)

print(x)
