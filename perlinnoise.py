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
     # print 'in perlin()'
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
"""
x = np.arange(10)
y = np.arange(10)
z = np.zeros([10,10])

for i in range (10):
     for j in range (10):
          z[i,j] = perlin(i,j)

plt.pcolormesh(x,y,z)
plt.colorbar()

plt.show()"""

def perlin2(x,y,seed=0):
    # permutation table
    np.random.seed(seed)
    p = np.arange(256,dtype=int)
    np.random.shuffle(p)
    #p = np.stack([p,p]).flatten()
    p = np.stack([p,p]).flatten()
    # coordinates of the top-left
    xi = x.astype(int)
    yi = y.astype(int)
    # internal coordinates
    xf = x - xi
    yf = y - yi
    # fade factors
    u = fade(xf)
    v = fade(yf)
    # noise components
    n00 = gradient(p[p[xi]+yi],xf,yf)
    n01 = gradient(p[p[xi]+yi+1],xf,yf-1)
    n11 = gradient(p[p[xi+1]+yi+1],xf-1,yf-1)
    n10 = gradient(p[p[xi+1]+yi],xf-1,yf)
    # combine noises
    x1 = lerp2(n00,n10,u)
    x2 = lerp2(n01,n11,u) # FIX1: I was using n10 instead of n01
    # print lerp2(x1,x2,v)
    # print len(lerp2(x1,x2,v))
    return lerp2(x1,x2,v) # FIX2: I also had to reverse x1 and x2 here

def lerp2(a,b,x):
    "linear interpolation"
    return a + x * (b-a)

def fade(t):
    "6t^5 - 15t^4 + 10t^3"
    return 6 * t**5 - 15 * t**4 + 10 * t**3

def gradient(h,x,y):
    "grad converts h to the right gradient vector and return the dot product with (x,y)"
    vectors = np.array([[0,1],[0,-1],[1,0],[-1,0]])
    g = vectors[h%4]
    return g[:,:,0] * x + g[:,:,1] * y

lin = np.linspace(0,5,100,endpoint=False)
x,y = np.meshgrid(lin,lin) # FIX3: I thought I had to invert x and y here but it was a mistake

# plt.imshow(perlin2(x,y,seed=2),origin='upper')












