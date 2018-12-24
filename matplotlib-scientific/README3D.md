from mpl_toolkits.mplot3d import Axes3D

Process:

 1: create a figure, fig = plt.figure() # not Figure

 2: get axea base on 3d , ax = Axes3D(fig)

 3: plot ax.plot_surface(x, y, z) # x, y is 1 dim, and z is 2 dim.

 4: show plt.show()
