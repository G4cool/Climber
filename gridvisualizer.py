import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint
import math

xMax, yMax = 150, 150
heightMax = 50
numHills = 10
descentDistance = 15
descentDistanceMultiplier = 3

x = np.arange(xMax)
y = np.arange(yMax)
z = np.zeros([xMax,yMax])
zVals = np.zeros([xMax,yMax])

for _ in range (numHills):
	xRand, yRand = randint(0,(xMax - 1)), randint(0,(yMax - 1))
	for i in range (descentDistance * descentDistanceMultiplier):
		for j in range (descentDistance * descentDistanceMultiplier):
			if (descentDistance*descentDistanceMultiplier/2 - i + xRand <= xMax) & (descentDistance*descentDistanceMultiplier/2 - j + yRand <= yMax):
				dist = math.sqrt(((descentDistance*descentDistanceMultiplier/2 - i)*(descentDistance*descentDistanceMultiplier/2 - i)) + ((descentDistance*descentDistanceMultiplier/2 - j)*(descentDistance*descentDistanceMultiplier/2 - j)))
				if dist == 0:
					if zVals[(descentDistance*descentDistanceMultiplier/2 - i + xRand - 1),(descentDistance*descentDistanceMultiplier/2 - j + yRand - 1)] == 0:
						z[(descentDistance*descentDistanceMultiplier/2 - i + xRand - 1),(descentDistance*descentDistanceMultiplier/2 - j + yRand - 1)] = heightMax
						zVals[(descentDistance*descentDistanceMultiplier/2 - i + xRand - 1),(descentDistance*descentDistanceMultiplier/2 - j + yRand - 1)] = heightMax
					else:
						z[(descentDistance*descentDistanceMultiplier/2 - i + xRand - 1),(descentDistance*descentDistanceMultiplier/2 - j + yRand - 1)] = heightMax + zVals[(descentDistance*descentDistanceMultiplier/2 - i + xRand - 1),(descentDistance*descentDistanceMultiplier/2 - j + yRand - 1)]
				else:
					if zVals[(descentDistance*descentDistanceMultiplier/2 - i + xRand - 1),(descentDistance*descentDistanceMultiplier/2 - j + yRand - 1)] == 0:
						z[(descentDistance*descentDistanceMultiplier/2 - i + xRand - 1),(descentDistance*descentDistanceMultiplier/2 - j + yRand - 1)] = 20 * (descentDistance*descentDistanceMultiplier/2)/dist
						zVals[(descentDistance*descentDistanceMultiplier/2 - i + xRand - 1),(descentDistance*descentDistanceMultiplier/2 - j + yRand - 1)] = 20 * (descentDistance*descentDistanceMultiplier/2)/dist
						# z[(descentDistance*descentDistanceMultiplier/2 - i + xRand - 1),(descentDistance*descentDistanceMultiplier/2 - j + yRand - 1)] = 1000
					else:
						z[(descentDistance*descentDistanceMultiplier/2 - i + xRand - 1),(descentDistance*descentDistanceMultiplier/2 - j + yRand - 1)] = 20 * (descentDistance*descentDistanceMultiplier/2)/dist + zVals[(descentDistance*descentDistanceMultiplier/2 - i + xRand - 1),(descentDistance*descentDistanceMultiplier/2 - j + yRand - 1)]
						# z[(descentDistance*descentDistanceMultiplier/2 - i + xRand - 1),(descentDistance*descentDistanceMultiplier/2 - j + yRand - 1)] = 1000

plt.pcolormesh(x,y,z)
plt.colorbar()

plt.show()











