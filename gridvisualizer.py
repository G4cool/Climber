"""import numpy as np
import matplotlib.pyplot as plt

# Make some random data to represent your r, g, b bands.
ny, nx = 2, 3
r, g, b = [np.random.random(ny*nx).reshape((ny, nx)) for _ in range(3)]

c = np.dstack([r,g,b])

plt.imshow(c, interpolation='nearest')
plt.show()"""
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, aspect='equal')
ax1.add_patch(
    patches.Rectangle(
        (0.1, 0.1),   # (x,y)
        0.5,          # width
        0.5,          # height
    )
)
fig1.savefig('rect1.png', dpi=90, bbox_inches='tight')"""
from pylab import *
plot([1,2,3])
show()