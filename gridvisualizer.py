import numpy as np
import matplotlib.pyplot as plt
from random import randint

# Make some random data to represent your r, g, b bands.
# ny, nx = 2, 3
# r, g, b = [np.random.random(ny*nx).reshape((ny, nx)) for _ in range(3)]
# r = [randint(0,72) for _ in range(3)];
r = [0 for _ in range(3)];
g = [randint(0,255) for _ in range (3)];
b = [0 for _ in range (3)];

c = np.dstack((r,g,b))

plt.imshow(c, interpolation='nearest')
plt.show()