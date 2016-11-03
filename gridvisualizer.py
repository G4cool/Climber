import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint
import math

xMax, yMax = 150, 150
heightMax = 50
numHills = 10
descentDistance = 15

x = np.arange(xMax)
y = np.arange(yMax)
z = np.zeros([xMax,yMax])

for _ in range (numHills):
	xRand, yRand = randint(0,(xMax - 1)), randint(0,(yMax - 1))
	for i in range (descentDistance):
		for j in range (descentDistance):
			if (descentDistance/2 - i + xRand <= xMax) & (descentDistance/2 - j + yRand <= yMax):
				dist = math.sqrt(((descentDistance/2 - i)*(descentDistance/2 - i)) + ((descentDistance/2 - j)*(descentDistance/2 - j)))
				if dist == 0:
					z[(descentDistance/2 - i + xRand - 1),(descentDistance/2 - j + yRand - 1)] = heightMax
				else:
					z[(descentDistance/2 - i + xRand - 1),(descentDistance/2 - j + yRand - 1)] = 20 * (descentDistance/2)/dist

plt.pcolormesh(x,y,z)
plt.colorbar()

plt.show()











