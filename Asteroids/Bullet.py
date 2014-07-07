__author__ = 'jmoran'

from Asteroids import MovingObject
from Asteroids.Colors import *


class Bullet(MovingObject):
    def __init__(self, window, game, init_point, slope):
        MovingObject.__init__(self, window, game, init_point, slope)
        self.frames = 0

    def draw(self):
        if self.frames % 2 == 0:
            x, y = self.point
            if x < 0 or x > self.wWidth or y < 0 or y > self.wHeight:
                return False
            rx, ry = self.slope
            self.point = (int(x - rx), int(y - ry))
            self.gObj = self.game.draw.circle(self.window, WHITE, self.point, 2)
        self.frames += 1

    def do_collision(self, obj):
        MovingObject.do_collision(self, obj)
        x, y = self.point
        self.game.draw.aaline(self.window, WHITE, (x-5, y), (x-10, y), 1)
        self.game.draw.aaline(self.window, WHITE, (x+5, y), (x+10, y), 1)

        self.game.draw.aaline(self.window, WHITE, (x, y-5), (x, y-10), 1)
        self.game.draw.aaline(self.window, WHITE, (x, y+5), (x, y+10), 1)

        self.game.draw.aaline(self.window, WHITE, (x+5, y+5), (x+10, y+10), 1)
        self.game.draw.aaline(self.window, WHITE, (x-5, y-5), (x-10, y-10), 1)

        self.game.draw.aaline(self.window, WHITE, (x+5, y-5), (x+10, y-10), 1)
        self.game.draw.aaline(self.window, WHITE, (x-5, y+5), (x-10, y+10), 1)
