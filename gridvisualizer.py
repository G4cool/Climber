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

xMax, yMax = 500, 500
heightMax = 50
numHills = 10
descentDistance = 150
descentDistanceMultiplier = 1
gradient = 10
distCorrection = math.sqrt(((descentDistance*descentDistanceMultiplier/2 - (descentDistance * descentDistanceMultiplier - 1))*(descentDistance*descentDistanceMultiplier/2 - (descentDistance * descentDistanceMultiplier - 1))) + ((descentDistance*descentDistanceMultiplier/2 - (descentDistance * descentDistanceMultiplier - 1))*(descentDistance*descentDistanceMultiplier/2 - (descentDistance * descentDistanceMultiplier - 1))))/gradient
heightCorrection = 20 * (descentDistance*descentDistanceMultiplier/2)/distCorrection
blurFactor = 0

x = np.arange(xMax)
print len(x)
y = np.arange(yMax)
z = np.zeros([xMax,yMax])
zVals = np.zeros([xMax,yMax])
# iterations = 300
# raiseList = spiral.asciiSpiral(iterations)
octaves = 3
# scaleFactor = 4
scaleTerrain = 10
perlinOctaves = []

for a in range (1, octaves + 1):
	print len(x)
	# print 'hi' + str(a)
	lin = np.linspace(0,5,xMax*a,endpoint=False)
	xPerlin,yPerlin = np.meshgrid(lin,lin) # FIX3: I thought I had to invert x and y here but it was a mistake

	w, h = xMax*a, yMax*a
	perlinArray = [[0 for i in range(w)] for j in range(h)]
	# scaledPerlinArray = [[0 for r in range(xMax*a)] for s in range(yMax*a)]

	seed = randint(1, 100)

	perlinArray = perlinnoise.perlin2(xPerlin,yPerlin,seed=2)
	"""
	for t in range(xMax*a):
		for u in range(yMax*a):
			scaledPerlinArray[t][u] = perlinArray[scaleFactor*t][scaleFactor*u]"""
	perlinOctaves.append(perlinArray) # WILL END W/ HIGHEST FREQUENCY
	# print perlinnoise.perlin2(x,y,seed=2)

for i in range(0, xMax):
	for j in range(0, yMax):
		for b in range (1, octaves + 1):
			# print 'hi' + str(b)
			z[i][j] += scaleTerrain*(octaves/b)*perlinOctaves[b-1][b * i][b * j]

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











