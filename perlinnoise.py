import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint
import random as random
import math

def lerp(a0, a1, w):
     return (1.0 - w)*a0 + w*a1

def dotGridGradient(ix, iy, x, y):
     # gradients = [[0 for x in range(99)] for y in range(99)]
     gradients = [];
     for i in range (99):
          for j in range (99):
               gradients.append((random.uniform(-1, 1),random.uniform(-1, 1)))

     dx = x - ix
     dy = y - iy

     # return (dx*gradients[iy][ix][0] + dy*gradients[iy][ix][1])
     return (dx*gradients[iy][ix] + dy*gradients[iy][ix])

def perlin(x, y):
     # x0 = (x > 0.0 ? x : x - 1)
     while x > 0:
          x = x - 1
     x0 = x
     x1 = x0 + 1
     # y0 = (y > 0.0 ? y : y - 1)
     while y > 0:
          y = y - 1
     y0 = y
     y1 = y0 + 1

     sx = x - x0
     sy = y - y0

     # n0, n1, ix0, ix1, value
     n0 = dotGridGradient(x0, y0, x, y)
     n1 = dotGridGradient(x1, y0, x, y)
     ix0 = lerp(n0, n1, sx)
     n0 = dotGridGradient(x0, y1, x, y)
     n1 = dotGridGradient(x1, y1, x, y)
     ix1 = lerp(n0, n1, sx)
     value = lerp(ix0, ix1, sy)

     return value

x = np.arange(100)
y = np.arange(100)
z = np.zeros([100,100])

for i in range (100):
     for j in range (100):
          z[i,j] = perlin(i,j)

plt.pcolormesh(x,y,z)
plt.colorbar()

plt.show()












