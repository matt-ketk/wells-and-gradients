class Well:
    def __init__(self, pos=(0,0)):
        self.pos = pos
        self.range = 0

    def dist(self,x,y):
        return ((self.pos[0] - x) ** 2 + (self.pos[1] - y) ** 2) ** 0.5

    def inRange(self, x, y):
        return (self.dist(x,y) <= self.range)

    def getPop(self, people_distro):
        popul = 0
        for x in range(people_distro.shape[0]):
            for y in range(people_distro.shape[1]):
                if self.inRange(x,y):
                    popul += int(100 * people_distro[x][y])

        return popul

    
    # water amount has 1:10 proportionality to radius