import numpy as np
RANGE_X = range(100)
RANGE_Y = range(100)
def calcCosts(well, people_distro):
    # return a tuple of 8 elements
    # iterate through each immediate possibility
    x = well.pos[0]
    y = well.pos[1]
    moveset = [
        (x-1,y+1), (x,y+1), (x+1,y+1),
        (x+1,y), (x+1,y-1), (x,y-1),
        (x-1,y-1),(x-1,y)
    ]
    pop_possibility = np.zeros(8)
    costs = np.zeros(8)
    for i in range(len(pop_possibility)):
        pop_possibility[i] = getPop(well, moveset[i], people_distro)
    
    for i in range(len(costs)):
        costs[i] = well.getPop(people_distro) - pop_possibility[i]

    return costs

def getLeast(a):
    least = a[0]
    ind = 0
    for i in range(len(a)):
        if a[i] < least:
            ind = i
            least = a[i]

    return ind

def getPop(well, pos, people_distro):
    popul = 0
    for x in range(people_distro.shape[0]):
        for y in range(people_distro.shape[1]):
            if inRange(well.range, x, pos[0], y, pos[1]):
                popul += int(people_distro[x][y])

    return popul

def inRange(r,x1,y1,x2,y2):
    return dist(x1,y1,x2,y2) <= r

def dist(x1,y1,x2,y2):
    return ((x1-x2) ** 2 + (y1-y2) ** 2) ** 0.5
def move(n, well):
    # n must be 0 to 8.
    x = well.pos[0]
    y = well.pos[1]
    moveset = [
        (x-1,y+1), (x,y+1), (x+1,y+1),
        (x+1,y), (x+1,y-1), (x,y-1),
        (x-1,y-1),(x-1,y)
    ]
    chosen = moveset[n]
    if withinLimits(chosen[0], chosen[1]):
        well.pos = moveset[n]

def withinLimits(x,y):
    return (x in RANGE_X) and (y in RANGE_Y)

def setLimits(sizex, sizey):
    RANGE_X = range(sizex)
    RANGE_Y = range(sizey)
