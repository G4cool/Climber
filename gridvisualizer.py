import matplotlib as mpl
import matplotlib.pyplot as pyplot
import numpy as np

# make values from -5 to 5, for this example
zvals = np.random.rand(100,100)*10-5

# make a color map of fixed colors
cmap = mpl.colors.ListedColormap(['black','green','white'])
bounds=[-6,-2,2,6]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

fig = pyplot.figure(2)

cmap2 = mpl.colors.LinearSegmentedColormap.from_list('my_colormap',
                                           ['black','green','white'],
                                           256)

img2 = pyplot.imshow(zvals,interpolation='nearest',
                    cmap = cmap2,
                    origin='lower')

pyplot.colorbar(img2,cmap=cmap2)

pyplot.show()











