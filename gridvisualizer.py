"""import numpy as np
import matplotlib.pyplot as plt
from random import randint

# Make some random data to represent your r, g, b bands.
# ny, nx = 2, 3
# r, g, b = [np.random.random(ny*nx).reshape((ny, nx)) for _ in range(3)]
# r = [randint(0,72) for _ in range(3)];
ny, nx = 3, 3
r = [0 for _ in range(3)];
g = [randint(0,255).reshape((ny, nx)) for _ in range (3)];
b = [0 for _ in range (3)];

c = np.dstack((r,g,b))

plt.imshow(c, interpolation='nearest')
plt.show()"""

import matplotlib as mpl
import matplotlib.pyplot as pyplot
import numpy as np

# make values from -5 to 5, for this example
zvals = np.random.rand(100,100)*10-5

# make a color map of fixed colors
cmap = mpl.colors.ListedColormap(['blue','black','red'])
bounds=[-6,-2,2,6]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

# tell imshow about color map so that only set colors are used
img = pyplot.imshow(zvals,interpolation='nearest',
                    cmap = cmap,norm=norm)

# make a color bar
pyplot.colorbar(img,cmap=cmap,
                norm=norm,boundaries=bounds,ticks=[-5,0,5])

pyplot.show()