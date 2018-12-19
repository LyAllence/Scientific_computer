#!/usr/bin/env python3
# coding: utf-8

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


class Plot3D(object):

    def __init__(self):
        self.x = np.arange(0, 20, 2)
        self.y = np.arange(0, 20, 2)
        # self.z = np.vstack(x) + y
        self.z = np.sqrt(self.x **2 + self.y)
        self.z = self.z.repeat(2)
        self.z = self.z.reshape(2,-1)

    def plot3d(self):
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.plot_surface(self.x, self.y, self.z)
        plt.show()


