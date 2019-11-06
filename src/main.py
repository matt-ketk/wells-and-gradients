import perlin_generator as pg
import greedy_method1 as gm1
from well import Well
import numpy as np
import numpy.random as rand

def main():
   greedy_method1(100)

    
def greedy_method1(iterations, sizex=100, sizey=100):
    

    people_distro = pg.create2DPerlinMap(sizex, sizey)
    water_distro = pg.create2DPerlinMap(sizex, sizey)
    popul_trend = np.zeros(iterations)

    well = Well(pos=(rand.randint(0,100), rand.randint(0,100)))
    well.range = 5 * water_distro[well.pos[0]][well.pos[1]]

    for i in range(iterations):
        gm1.move(gm1.getLeast(gm1.calcCosts(well, people_distro)), well)
        well.range = 5 * int(water_distro[well.pos[0]][well.pos[1]])
        # popul_trend[i] = well.getPop(people_distro)
        print(well.getPop(people_distro))
    # return popul_trend
        
if __name__ == "__main__":
    main()