import spiral
import perlinnoise
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint
import math
from random import randint
# import pyglet
# from scipy.ndimage.filters import gaussian_filter

xMax, yMax = 100, 100
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
iterations = 300
raiseList = spiral.asciiSpiral(iterations)

lin = np.linspace(0,5,100,endpoint=False)
x,y = np.meshgrid(lin,lin) # FIX3: I thought I had to invert x and y here but it was a mistake

w, h = 100, 100
perlinArray = [[0 for i in range(w)] for j in range(h)]

seed = randint(1, 100)

perlinArray = perlinnoise.perlin2(x,y,seed=seed)
# print perlinnoise.perlin2(x,y,seed=2)

for i in range(0, 100):
	for j in range(0, 100):
		z[i][j] += perlinArray[i][j]

"""
for i in range(-1*xMax, xMax):
	for j in range(-1*yMax, yMax):
		z[i][j] += perlinnoise.perlin(i, j)"""

"""
for i in range(-1*xMax, xMax):
	for j in range(-1*yMax, yMax):
		for k in range(iterations):
			if raiseList[k][0] == i and raiseList[k][1] == j:
				z[i][j] += heightMax
"""

"""
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
"""

# blurredZ = gaussian_filter(z, sigma=5)

plt.pcolormesh(x,y,z, cmap='Greens_r')
plt.colorbar()

"""
win = pyglet.window.Window()
 
@win.event
def on_draw():
        win.clear()
 
pyglet.app.run()"""

plt.show()











