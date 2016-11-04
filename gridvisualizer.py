import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint
import math
from scipy.ndimage.filters import gaussian_filter

xMax, yMax = 150, 150
heightMax = 50
numHills = 10
descentDistance = 150
descentDistanceMultiplier = 1
gradient = 10
distCorrection = math.sqrt(((descentDistance*descentDistanceMultiplier/2 - (descentDistance * descentDistanceMultiplier - 1))*(descentDistance*descentDistanceMultiplier/2 - (descentDistance * descentDistanceMultiplier - 1))) + ((descentDistance*descentDistanceMultiplier/2 - (descentDistance * descentDistanceMultiplier - 1))*(descentDistance*descentDistanceMultiplier/2 - (descentDistance * descentDistanceMultiplier - 1))))/gradient
heightCorrection = 20 * (descentDistance*descentDistanceMultiplier/2)/distCorrection
blurFactor = 0

x = np.arange(xMax)
y = np.arange(yMax)
z = np.zeros([xMax,yMax])
zVals = np.zeros([xMax,yMax])

for _ in range (numHills):
	xRand, yRand = randint(0,(xMax - 1)), randint(0,(yMax - 1))
	for i in range (descentDistance * descentDistanceMultiplier):
		for j in range (descentDistance * descentDistanceMultiplier):
			if (descentDistance*descentDistanceMultiplier/2 - i + xRand <= xMax) & (descentDistance*descentDistanceMultiplier/2 - j + yRand <= yMax):
				dist = math.sqrt(((descentDistance*descentDistanceMultiplier/2 - i)*(descentDistance*descentDistanceMultiplier/2 - i)) + ((descentDistance*descentDistanceMultiplier/2 - j)*(descentDistance*descentDistanceMultiplier/2 - j)))/gradient
				if dist == 0:
					z[(descentDistance*descentDistanceMultiplier/2 - i + xRand - 1),(descentDistance*descentDistanceMultiplier/2 - j + yRand - 1)] = heightMax - heightCorrection + z[(descentDistance*descentDistanceMultiplier/2 - i + xRand - 1),(descentDistance*descentDistanceMultiplier/2 - j + yRand - 1)]
					zVals[(descentDistance*descentDistanceMultiplier/2 - i + xRand - 1),(descentDistance*descentDistanceMultiplier/2 - j + yRand - 1)] += heightMax
				else:
					z[(descentDistance*descentDistanceMultiplier/2 - i + xRand - 1),(descentDistance*descentDistanceMultiplier/2 - j + yRand - 1)] = 20 * (descentDistance*descentDistanceMultiplier/2)/dist - heightCorrection + zVals[(descentDistance*descentDistanceMultiplier/2 - i + xRand - 1),(descentDistance*descentDistanceMultiplier/2 - j + yRand - 1)]
					zVals[(descentDistance*descentDistanceMultiplier/2 - i + xRand - 1),(descentDistance*descentDistanceMultiplier/2 - j + yRand - 1)] += 20 * (descentDistance*descentDistanceMultiplier/2)/dist

if blurFactor != 0:
	for k in range (xMax):
		for l in range (yMax):
			sumVals = 0
			counter = 0
			if l - blurFactor >= 0:
				if k - blurFactor >= 0:
					sumVals += z[(k - blurFactor),(l - blurFactor)]
					counter += 1
				sumVals += z[(k),(l - blurFactor)]
				counter += 1
				if k + blurFactor < 150:
					sumVals += z[(k + blurFactor),(l - blurFactor)]
					counter += 1
			if k - blurFactor >= 0:
				sumVals += z[(k - blurFactor),(l)]
				counter += 1
			sumVals += z[(k),(l)]
			counter += 1
			if k + blurFactor < 150:
				sumVals += z[(k + blurFactor),(l)]
				counter += 1
			if l + blurFactor < 150:
				if k - blurFactor >= 0:
					sumVals += z[(k - blurFactor),(l + blurFactor)]
					counter += 1
				sumVals += z[(k),(l + blurFactor)]
				counter += 1
				if k + blurFactor < 150:
					sumVals += z[(k + blurFactor),(l + blurFactor)]
					counter += 1

			average = sumVals/counter
			z[(k),(l)] = average

plt.pcolormesh(x,y,z)
plt.colorbar()

plt.show()











