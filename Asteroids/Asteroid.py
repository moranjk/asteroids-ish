__author__ = 'jmoran'

from Asteroids import MovingObject
from Asteroids.Colors import *
from random import getrandbits, randint
from math import sin, cos, radians


class Asteroid(MovingObject):
    def __init__(self, window, game, init_point, size):
        slope = (1 if getrandbits(1) else -1, 1 if getrandbits(1) else -1)
        MovingObject.__init__(self, window, game, init_point, slope)
        self.size = size
        x, y = self.point
        self.points = []
        for d in range(0, 360, 30):
            r = randint(int(size/2), size)
            p = (x + (r * cos(radians(d))), y + (r * sin(radians(d))))
            self.points.append(p)

    def draw(self):
        x, y = self.point
        rx, ry = self.slope
        x = int(x - rx)
        y = int(y - ry)

        if x > self.wWidth:
            x -= self.wWidth
            self.points = tuple((x1-self.wWidth, y1-ry) for (x1, y1) in self.points)
        elif x < 0:
            x += self.wWidth
            self.points = tuple((x1+self.wWidth, y1-ry) for (x1, y1) in self.points)
        elif y > self.wHeight:
            y -= self.wHeight
            self.points = tuple((x1, y1-self.wHeight) for (x1, y1) in self.points)
        elif y < 0:
            y += self.wHeight
            self.points = tuple((x1, y1+self.wHeight) for (x1, y1) in self.points)
        else:
            self.points = tuple((x1-rx, y1-ry) for (x1, y1) in self.points)

        self.point = (x, y)

        self.gObj = self.game.draw.aalines(self.window, WHITE, True, self.points, 1)

    def do_collision(self, obj):
        MovingObject.do_collision(self, obj)
        size = int(self.size / 1.5)
        if size > 15:
            return [Asteroid(self.window, self.game, tuple(p + 2 for p in self.point), size),
                    Asteroid(self.window, self.game, self.point, size),
                    Asteroid(self.window, self.game, tuple(p - 2 for p in self.point), size)]
        else:
            return []
