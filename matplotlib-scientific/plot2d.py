# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as pmg

class Plot2d(object):

    def __init__(self):
        self.x = np.linspace(0, 4, num=100)

    # don't create figure, system will give me a defualt figure.
    def no_figure(self):
        plt.plot(self.x, self.x ** 2, 'g-')
        plt.title('No Create Figure! ')
        plt.xlabel('X label')
        plt.ylabel('Y label')
        plt.show()

    # create figure, and we can have more than one figure.
    def have_figure(self):
        figure_single = plt.Figure() # no axes and no graphics
        figure_sub, xls = plt.subplots(2,1)
        xls[0].plot(self.x, self.x ** 2, 'ro')
        xls[1].plot(self.x, self.x ** 3, 'b--')
        figure_sub.suptitle('Figure')
        plt.show()

    # we can change x or y length
    def set_dim(self):
        plt.plot(self.x, self.x ** 2, 'g-')
        plt.ylim([0,20])
        plt.xlim([0,8])
        plt.show()
        # or
        figure_sub, xls = plt.subplots(2,1)
        xls[1].plot(self.x, self.x ** 3, 'b--')
        xls[1].axis([0,8,0,20])
        plt.show()

    # there are some other method to show graphic.
    def other_plot(self):
        plt.bar(self.x, np.random.randint(10, size=(100,)))
        plt.show()
        
        plt.hist(self.x)
        plt.show()
        
        img = pmg.imread('./1.png')
        plt.imshow(img)




