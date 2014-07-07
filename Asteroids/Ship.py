__author__ = 'jmoran'

from Asteroids import Object, Bullet
import math

from Asteroids.Colors import *


class Ship(Object):
    radius = 10

    def __init__(self, window, game):
        Object.__init__(self, window, game)
        self.point = (self.wWidth / 2, self.wHeight / 2)
        self.start_point = self.point
        self.radians = tuple(math.radians(x) for x in (270, 30, 90, 150))
        self.start_radians = self.radians
        self.acceleration = 0
        self.heading = None
        self.frames = 0
        self.crashed = False
        self.crash_time = 0
        self.crash_point = None

    def turn_left(self):
        self.radians = tuple(p - math.radians(15) for p in self.radians)

    def turn_right(self):
        self.radians = tuple(p + math.radians(15) for p in self.radians)

    def accelerate(self):
        if self.heading == self.radians[0]:
            self.acceleration += 0.04
        else:
            self.heading = self.radians[0]

    def decelerate(self):
        self.acceleration -= 0.04
        if self.acceleration < 0:
            self.acceleration = 0

    def draw(self):
        if self.crashed:
            self.draw_crash()
        else:
            self.gObj = self.game.draw.aalines(self.window, WHITE, True, self.get_points(), 1)

    def move(self, point):
        x, y = point
        if x > self.wWidth:
            x -= self.wWidth
        elif x < 0:
            x += self.wWidth
        elif y > self.wHeight:
            y -= self.wHeight
        elif y < 0:
            y += self.wHeight
        self.point = (x, y)

    def fire(self):
        a = self.radians[0]
        r = self.radius
        x, y = self.point
        x2, y2 = (x + (r * math.cos(a)), y + (r * math.sin(a)))
        return Bullet(self.window, self.game, (x2, y2), (x - x2, y - y2))

    def get_points(self):
        x, y = self.point
        r = self.radius
        if self.acceleration > 0 and self.heading is not None:
            a = self.heading
            x2, y2 = (x + (r * math.cos(a)), y + (r * math.sin(a)))
            self.move((x - ((x - x2) * self.acceleration), y - ((y - y2) * self.acceleration)))
            x, y = self.point
        p0 = (x + (r * math.cos(self.radians[0])), y + (r * math.sin(self.radians[0])))
        p1 = (x + (r * math.cos(self.radians[1])), y + (r * math.sin(self.radians[1])))
        p2 = (x + ((r / 4) * math.cos(self.radians[2])), y + ((r / 4) * math.sin(self.radians[2])))
        p3 = (x + (r * math.cos(self.radians[3])), y + (r * math.sin(self.radians[3])))
        return p0, p1, p2, p3

    def reset(self):
        self.point = self.start_point
        self.radians = self.start_radians
        self.acceleration = 0
        self.heading = None
        self.crashed = False
        self.no_collide = False

    def draw_crash(self):
        x, y = self.crash_point
        self.game.draw.aaline(self.window, WHITE, (x-5, y), (x-10, y), 1)
        self.game.draw.aaline(self.window, WHITE, (x+5, y), (x+10, y), 1)

        self.game.draw.aaline(self.window, WHITE, (x, y-5), (x, y-10), 1)
        self.game.draw.aaline(self.window, WHITE, (x, y+5), (x, y+10), 1)

        self.game.draw.aaline(self.window, WHITE, (x+5, y+5), (x+10, y+10), 1)
        self.game.draw.aaline(self.window, WHITE, (x-5, y-5), (x-10, y-10), 1)

        self.game.draw.aaline(self.window, WHITE, (x+5, y-5), (x+10, y-10), 1)
        self.game.draw.aaline(self.window, WHITE, (x-5, y+5), (x-10, y+10), 1)

    def do_collision(self, obj):
        Object.do_collision(self, obj)
        self.no_collide = True
        self.crashed = True
        self.crash_point = self.point
