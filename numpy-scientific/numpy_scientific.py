#!/usr/bin/env python3
# coding: utf-8

import numpy as np


# there are some method create ndarray(this is the storage unit in np)
class Create_ndarray():

    # the method will return ndarray be created with list or tuple
    def from_iterator(self, dataset):
        assert isinstance(dataset, list) or isinstance(dataset, tuple), "the dataset is invalid"
        print(np.array(dataset))

    # there are some create method
    def from_method(self):
        # arange(start, stop, step, dtype) 
        arr = np.arange(1, 20, 3)
        print('arang', arr)
        # linspace(start, stop, num=50, endpoint=True, ...)
        lis = np.linspace(1, 20, num=5)
        print('linspace', lis)
        # logspaces(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
        lgs = np.logspace(1, 2, num=5)
        print('logspace', lgs)

    # there are some data from file
    def from_file(self):
        f = open('file.data', 'r')
        # genfromtxt(f, delimiter, autostrip=False, skip_header=0, skip_footer=0, usecols=(m,n)) get data from file
        data = np.genfromtxt(f)
        print('fileData', data)

    # there are some attribute.
    def some_attribute(self):
        arr = np.arange(1, 20, 3)
        print('dtype', arr.dtype)
        print('itemsize', arr.itemsize)
        print('ndim', arr.ndim)
        print('real.data', arr.real)
        print('size', arr.size)
        print('shape', arr.shape)

    # there are some method of np
    def some_method(self):
        arr = np.arange(1, 20, 2)
        print('sub ndarray', arr[2:])
        # this only can use with one ndim.
        print('specify line', arr[[n,m]])
        print('repeat', arr.repeat(3))
        print('tile', np.tile(arr, 4))
        # we need reshape the ndarray, we will use more ndim matrix.
        arr = arr.reshape(5, -1)
        print('reshape', arr)
        print('Transpose', arr.transpose())
        # or
        print('T', arr.T)
        # and we need get two matrix, use np.split
        arr1, arr2 = np.split(arr, 2)
        print('vstack', np.vstack([arr1,arr2]))
        # or
        print('r_', np.r_[arr1, arr2])
        print('hstack', np.hstack([arr1,arr2]))
        # or
        print('C_', np.c_[arr1, arr2])
        print('same, 1 2', np.intersect1d(arr1,arr2))
        print('same, 1 1', np.intersect1d(arr1,arr1))
        print('diff, 1 1', np.setdiff1d(arr1, arr1))
        print('diff, 1 2', np.setdiff1d(arr1, arr2))

        # there is solve math problem, and y = ax
        a = np.array([[1, 2], [2, 3]])
        b = np.array([4, 25])
        print('solve', np.linalg.solve(a, b))

        # compute arr1, arr2
        print('arr1 + arr2', arr1 + arr2)
        print('arr1 - arr2', arr1 - arr2)
        print('arr1 * arr2', arr1 * arr2) # this is multiply(math)
        print('arr1 / arr2', arr1 / arr2)
        print('arr1 dot arr2', arr1.dot(arr2.T))

