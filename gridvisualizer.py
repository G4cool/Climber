#!usr/env/python3
import numpy as np
import matplotlib.pyplot as plt

# Make some random data to represent your r, g, b bands.
ny, nx = 2, 3
r, g, b = [np.random.random(ny*nx).reshape((ny, nx)) for _ in range(3)]

c = np.dstack([r,g,b])

plt.imshow(c, interpolation='nearest')
plt.show()