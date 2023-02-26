import random

class Particle:
    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.vx = 0.0
        self.vy = 0.0
        
        self.x = random.uniform(self.min, self.max)
        self.xb = self.x
        self.y = random.uniform(self.min, self.max)
        self.yb = self.y
        
        
    def __f(self, x, y):
        return (pow(x + 2*y - 7, 2)) + (pow(2*x + y - 5, 2))

    def move(self):
        self.x += self.vx
        if self.x > self.max:
            self.x = self.max-0.5
        if self.x < self.min:
            self.x = self.min+0.5
            
        self.y += self.vy
        if self.y > self.max:
            self.y = self.max-0.5
        if self.y < self.min:
            self.y = self.min+0.5

    def find_best(self, xgb, ygb):
        if self.__f(self.x, self.y) < self.__f(self.xb, self.yb):
            self.xb = self.x
            self.yb = self.y
        if self.__f(self.xb, self.yb) < self.__f(xgb, ygb):
            xgb = self.xb
            ygb = self.yb
            
        return xgb, ygb

    def update_speed(self, xgb, ygb):
        r1 = random.random()
        r2 = random.random()
        self.vx = 0.05 * r1 * (self.xb - self.x) + 0.05 * r2 * (xgb - self.x)
        self.vy = 0.05 * r1 * (self.yb - self.y) + 0.05 * r2 * (ygb - self.y)

    def tick(self, xgb, ygb):
        self.update_speed(xgb, ygb)
        self.move()
        return self.find_best(xgb, ygb)
        