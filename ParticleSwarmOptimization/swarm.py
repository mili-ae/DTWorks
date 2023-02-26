from particle import Particle
from sys import maxsize

class Swarm:
    def __init__(self, count):
        self.xs = list()
        self.ys = list()
        self.particles = list()
        self.xgb = maxsize
        self.ygb = maxsize
        
        for i in range(count):
            self.particles.append(Particle(-10, 10))
            self.xs.append(self.particles[i].x)
            self.ys.append(self.particles[i].y)

    def f(self, x, y):
        return (pow(x + 2*y - 7, 2)) + (pow(2*x + y - 5, 2))

    def tick(self):
        for i in self.particles:
            self.xgb, self.ygb = i.tick(self.xgb, self.ygb)

        self.xs = list()
        self.ys = list()
        for i in range(len(self.particles)):
            self.xs.append(self.particles[i].x)
            self.ys.append(self.particles[i].y)
        return self.xs, self.ys


    def __str__(self) -> str:
        string = ""
        for i in self.particles:
            string += f"{i.x}, {i.y}\n"
            
        return string
    