import matplotlib.pyplot as plt

process:

 1: create a figure (only use one times, after using will clean) or not use, if not, all process only have one figure(default)

 2: plot data, see graphics please.

guide:

 1: figure: in all screen.

 2: axes: area in figure.

 3: axis: x or y dim in axes.

 4: artist: our graphics.

create figure:

 1: plt.Figure() # simple figure, empty figure without axes

 2: fig, lst = plt.subplots(m=1, n=1) # a figure with a m x n grid of axes. lst is a tuple.

graphics setting:

 1: plt.cla() # append a figure.

 2: plt.clf() # clear current figure.

 3: plt.close() # close current figure.

graphics:

 1: plt.plot(x, y, 'bo') or lst.plot(x, y, 'bo') # x and y are iterator(list or tuple or np.array etc. 'bo' is the graphics's format, b is blue, o is circle.) and we can write both => plt.plot(x1, y1, 'bo', x2, y2, 'bo') 

 2: plt.bar(x, height, width=0.8,..) # plot bar. and plt.barh is horizontal.

 3: plt.hist(x,..) # plot a histogram.

 4: plt.imshow(img) # show img, img is a image char. exp: matplotlib.image.imread(file_string) 

setting:

 1: fig.suptitle(title) # set title

 2: lst.set_xlabel(flag) or lst.set_ylabel(flag) or plt.xlabel or plt.ylabel# set flag of x or y

 3: lst.set_xlim(n) or lst.set_ylim(n) # set axes of fig, default is 1

 4: matplotlib.rcParams['xxx']=xxx # set matplotlib attribute.

 5: plt.axis([x1, x2, y1, y2]) # set viewport in axes

 6: plt.plot(x, y, 'bo', linewidth=x) or f, = plt.plot(x, y, 'bo') & f.set _ linewidth(x) or plt.setp(f, linewidth=3) or plt.setp(f, 'linewidth', 2).

 7: plt.text(x, y, text) # set text in figure.

 8: plt.grid(True) # use grid.

 9：plt.annotate(text, xy,xytext,...) # annotate, xy is the end point. xytext is the begin point.

 10: plt.yscale(x) # set scale

 11: plt.imshow(img, cmap=xx, clim=(n,m)) # set colormap or cut area, ex: hot, jet, et. or p = plt.imshow(img), p.set_cmap(xx) p.set_clim()

 12: plt.colorbar() # get color table

tip:

 1: plt.ion() # can interactive after plotting. and no plt.show().

 2: plt.ioff() # all lines will be shown sometime and must run plt.show()

 3: plt.plot('a', 'b', data=data) data is a dict, 'a' 'b' is the dict's key.

 4: plt.figure(1, figsize=(9, 3)) # set figure have 3 axes.

 5: plt.subplot(211) is same to plt.subplot(2, 1, 1)

 6: plt.legend(hearders=x) # add graphics to a fig after the fig have a graphics.


