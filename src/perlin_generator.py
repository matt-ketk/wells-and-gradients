import numpy as np
import matplotlib.pyplot as plt
import time as time


def perlin(x,y,seed=1):
    # permutation table
    np.random.seed(seed)
    p = np.arange(256,dtype=int)
    np.random.shuffle(p)
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
    x1 = lerp(n00,n10,u)
    x2 = lerp(n01,n11,u) # FIX1: I was using n10 instead of n01
    return lerp(x1,x2,v) # FIX2: I also had to reverse x1 and x2 here

def lerp(a,b,x):
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
"""
lin = np.linspace(0,5,100,endpoint=False)
x,y = np.meshgrid(lin,lin) # FIX3: I thought I had to invert x and y here but it was a mistake
"""
def create2DPerlinMap(sizeX, sizeY, density_constant=100): # LATER: understand how perlin noise works, modify function to be more customizable accordingly
    xlin = np.linspace(0, sizeX, density_constant)
    ylin = np.linspace(0, sizeY, density_constant)
    x,y = np.meshgrid(xlin,ylin)
    return perlin(x,y,seed=int(time.time()))

def floorifyMap(p_map):
    for x in range(p_map.shape[0]):
        for y in range(p_map.shape[1]):
            if p_map[x][y] < 0.0:
                p_map[x][y] = 0.0
                    

"""
test_map = create2DPerlinMap(10,10)
floorifyMap(test_map)
for x in np.nditer(50 * test_map):
    print(int(x))

plt.imshow(perlin(x,y,seed=1),origin='upper')
plt.show()
"""